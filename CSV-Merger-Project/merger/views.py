import pandas as pd

from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CSVUploadForm
from .models import MergedDataSet

# Create your views here.
CHUNK_SIZE = 50_000
ROWS_PER_PAGE = 100

# Uploading and concatenating CSV files row by row (pandas axis=0).
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = form.cleaned_data['csv_files']
            dataframes = []
            valid_file_count = 0
            warnings = []

            for f in uploaded_files:
                if not f.name.lower().endswith('.csv'):
                    warnings.append(f"Skipped '{f.name}' — not a .csv file.")
                    continue
                try:
                    # Read in chunks to limit memory use for each uploaded file.
                    chunks = list(pd.read_csv(f, chunksize=CHUNK_SIZE))
                    if not chunks:
                        warnings.append(f"Skipped '{f.name}': the CSV has no data or columns.")
                        continue
                    dataframes.extend(chunks)
                    valid_file_count += 1
                except Exception as exc:
                    warnings.append(f"Could not read '{f.name}': {exc}")

            if not dataframes:
                messages.error(request, "No valid CSV files were uploaded.")
                return redirect('upload_csv')

            # axis=0 appends rows. ignore_index=True creates a fresh 0..N-1
            # index. sort=False keeps first-seen column order; absent columns
            # are blank in the saved CSV.
            merged_df = pd.concat(dataframes, axis=0, ignore_index=True, sort=False)

            dataset = MergedDataSet(
                name=f"Merge of {len(dataframes)} file(s) — {merged_df.shape[0]} rows",
                source_file_count=valid_file_count,
                row_count=len(merged_df),
                colm_count=len(merged_df.columns),
            )
            csv_text = merged_df.to_csv(index=False)
            dataset.merged_file.save(
                'merged_dataset.csv',
                ContentFile(csv_text.encode('utf-8')),
                save=True,
            )

            for w in warnings:
                messages.warning(request, w)
            messages.success(request, "Files merged successfully.")
            return redirect('view_dataset', pk=dataset.pk)
    else:
        form = CSVUploadForm()

    recent_datasets = MergedDataSet.objects.all()[:10]
    return render(
        request,
        'merger/upload.html',
        {'form': form, 'recent_datasets': recent_datasets},
    )

# Displaying Dataset
def view_dataset(request, pk):
    dataset = get_object_or_404(MergedDataSet, pk=pk)

    # Read only the merged file's row count up front is cheap; for display
    # we still page through it so the browser never receives more than
    # ROWS_PER_PAGE rows at a time.
    df = pd.read_csv(dataset.merged_file.path)

    paginator = Paginator(range(len(df)), ROWS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    start = page_obj.start_index() - 1
    end = page_obj.end_index()
    page_df = df.iloc[start:end]

    return render(
        request,
        'merger/result.html',
        {
            'dataset': dataset,
            'columns': df.columns.tolist(),
            'rows': page_df.values.tolist(),
            'page_obj': page_obj,
        },
    )
