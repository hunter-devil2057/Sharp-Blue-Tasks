from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField(max_length=9000)
    image = models.ImageField(upload_to="blog_images/")
    content = models.CharField(max_length=30000000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    CATEGORY_CHOICES = [
        ("politics", "Politics"),
        ("economy", "Economy"),
        ("society", "Society"),
        ("world", "World"),
        ("op-ed", "OP-ED"),
        ("sports", "Sports"),
        ("diaspora", "Diaspora"),
        ("market", "Market"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.title

# Comments Model
class Comment(models.Model):
    posts = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.posts.title}"