import Entities
import requests
import shutil
import os.path

class Pokemon(Entities.Entity):
	def __init__(self, pokemonID):
		super(Pokemon, self).__init__()

		# download the pokemon
		self._BASEURL = "http://pokeapi.co"
		r = requests.get(self._BASEURL + '/api/v1/pokemon/' + str(pokemonID) + "/")

		if r.status_code == 200:
   			self.buildStatus = True

   			self._json = r.json()
			self.name = self._json["name"]
			self.stats.hp = self._json["hp"]
			
			# maigc power and magic resistance will be the max power and resistance of the pokemon
			if self._json["attack"] > self._json["sp_atk"]:
				self.stats.magicPower = self._json["attack"]
			else:
				self.stats.magicPower = self._json["sp_atk"]
			if self._json["defense"] > self._json["sp_def"]:
				self.stats.magicResistance = self._json["defense"]
			else:
				self.stats.magicResistance = self._json["sp_def"]

			# now we need to set the sprite
			self._setSprite(self._BASEURL + self._json["sprites"][0]["resource_uri"])

		else:
			self.buildStatus = False

	# this will get the sprite and set it
	def _setSprite(self, url):
		r = requests.get(url)
		if r.status_code == 200:
			self.buildStatus = True
			resources = r.json()
			self._imageURL = resources["image"]
			self._imagePath = os.path.join("resources", "pokemonSprites", self.name + ".png")

			# download sprite
			response = requests.get(self._BASEURL + self._imageURL, stream=True)
			if response.status_code == 200:
				with open(self._imagePath, 'wb') as out_file:
					shutil.copyfileobj(response.raw, out_file)
					del response
			else:
				self.buildStatus = False
		else:
			self.buildStatus = False
