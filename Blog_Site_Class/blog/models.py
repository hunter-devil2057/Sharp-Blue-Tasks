from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=90000)
    image = models.ImageField(upload_to='blog_images/')
    content = models.CharField(max_length=3000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    likes = models.PositiveBigIntegerField(default = 0)

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
        max_length=25, 
        choices=CATEGORY_CHOICES
        )

    def __str__(self):
        return self.title

# Comment Models
class Comment(models.Model):
    posts = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.posts.title}"