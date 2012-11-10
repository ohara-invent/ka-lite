import uuid
from django.db import models
from securesync.models import SyncedModel, FacilityUser
import settings

class VideoLog(SyncedModel):
    user = models.ForeignKey(FacilityUser, blank=True, null=True, db_index=True)
    youtube_id = models.CharField(max_length=11, db_index=True)
    total_seconds_watched = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    def get_uuid(self, *args, **kwargs):
        namespace = uuid.UUID(self.user.id)
        return uuid.uuid5(namespace, str(self.youtube_id)).hex

class ExerciseLog(SyncedModel):
    user = models.ForeignKey(FacilityUser, blank=True, null=True, db_index=True)
    exercise_id = models.CharField(max_length=50, db_index=True)
    streak_progress = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    def get_uuid(self, *args, **kwargs):
        namespace = uuid.UUID(self.user.id)
        return uuid.uuid5(namespace, str(self.exercise_id)).hex

settings.add_syncing_models([VideoLog, ExerciseLog])

class VideoFile(models.Model):
    youtube_id = models.CharField(max_length=11, primary_key=True)
    flagged_for_download = models.BooleanField(default=False)
    download_in_progress = models.BooleanField(default=False)
    percent_complete = models.IntegerField(default=0)
