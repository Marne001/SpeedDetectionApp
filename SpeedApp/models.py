from django.db import models
from django.urls import reverse
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.layers.experimental import preprocessing
import pandas as pd
from keras.models import load_model
from decimal import Decimal


class SpeedModel(models.Model):
    EngineKW  = models.DecimalField(decimal_places=5, max_digits=20)
    EngineRPM = models.DecimalField(decimal_places=5, max_digits=20)
    Horsepower = models.DecimalField(decimal_places=5, max_digits=20)
    Torque = models.DecimalField(decimal_places=5, max_digits=20)
    Speed = models.TextField()

    def get_absolute_url(self):
        return reverse('SpeedApp:speed-detail', kwargs={'pk':self.pk})


    def save(self, *args, **kwargs):
        self.calculate_speed()
        super().save(*args, **kwargs)

    def calculate_speed(self, *args, **kwargs):
        #sp = self.AbsoluteThrottlePosition + self.EngineKW + self.EngineRPM + self.FfrHour + self.FfrM + self.Torque + self.Horsepower
        #self.Speed = sp

        #data = [[self.EngineKW, self.EngineRPM, self.Torque, self.Horsepower]]
        data = np.array([[self.EngineKW, self.EngineRPM, self.Horsepower, self.Torque]]).astype('float32')
        #print(self.EngineKW, self.EngineRPM, self.Horsepower, self.Torque)
        #df = pd.DataFrame(data, columns = ['EngineKW', 'EngineRPM', 'Horsepower', 'Torque'])
        #print(df)
        #print(df.shape)
        #normalizer = preprocessing.Normalization(axis=-1)
        #normalizer.adapt(np.array(df))

        sp = load_model('dnn_model2')
        #print(sp.summary())
        result = sp.predict(data)
        self.Speed = str(result[0][0])

        


