from django.db import models
from users.models import Profile
import uuid


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    # null - can be empty in database, blank - form field can be empty
    description = models.TextField(null=True, blank=True) 
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,
        primary_key=True, # use this field as primary key
        editable=False, # cannot modify this in forms
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-vote_ratio', '-vote_total', 'title']

    @property
    def image_URL(self):
        try: 
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        return self.review_set.all().values_list('owner__id', flat=True)


    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count()

        ratio = int((up_votes / total_votes) * 100)
        self.vote_total = total_votes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True) 
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,
        primary_key=True, # use this field as primary key
        editable=False, # cannot modify this in forms
        )

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value

        
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,
        primary_key=True, # use this field as primary key
        editable=False, # cannot modify this in forms
        )
    
    def __str__(self):
        return self.name

        
     