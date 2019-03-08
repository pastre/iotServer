from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length = 160)

	def __str__(self):
		return self.name

class Device(models.Model):
	ipAddress = models.CharField(max_length = 16)
	name = models.CharField(max_length = 160)
	description = models.CharField(max_length = 500, default = 'No description provided')
	states = models.ManyToManyField(State)
	currentState = models.IntegerField(default = 0)
	isDirty = models.BooleanField(default = True)

	def asResponse(self):
		return {
			'name' : self.name,
			'description' : self.description,
			'currentState' : self.currentState,
			'id': self.id,
		}
	def getStates(self):
		return [i for i in self.states.iterator()]

	def currentOp(self):
		return self.getStates()[self.currentState].name

	def passOp(self):
		self.currentState += 1
		print('My state is', self.currentState, 'I have', self.states.count(), 'states')
		if self.currentState >= self.states.count():
			print('I need to reset my state')
			self.currentState = 0
		self.save()

	def __str__(self):
		return self.name
