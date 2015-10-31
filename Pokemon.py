import Entities
import requests
import shutil
import os.path

class Pokemon(Entities.Entity):
	def __init__(self, pokemonID):
		super(Pokemon, self).__init__()

		# if the data file already exists then use it
		self._pokemonDataFile = "pokemon" + str(pokemonID) + ".pokedat"
		if os.path.isfile(self._pokemonDataFile):
			# load the pokemon .pokedat file
			pass
		else:
			# download the files
			self._downloadPokemon(pokemonID)
		
		
	def _downloadPokemon(self, pokemonID):
		# download the pokemon
		print "downloading pokemon data"
		self._BASEURL = "http://pokeapi.co"
		r = requests.get(self._BASEURL + '/api/v1/pokemon/' + str(pokemonID) + "/")

		if r.status_code == 200:
   			self.buildStatus = True

   			json = r.json()
			self.name = json["name"]
			self.stats.hp = json["hp"]
			
			# maigc power and magic resistance will be the max power and resistance of the pokemon
			if json["attack"] > json["sp_atk"]:
				self.stats.magicPower = json["attack"]
			else:
				self.stats.magicPower = json["sp_atk"]
			if json["defense"] > json["sp_def"]:
				self.stats.magicResistance = json["defense"]
			else:
				self.stats.magicResistance = json["sp_def"]

			# now we need to set the sprite
			self._setSprite(self._BASEURL + json["sprites"][0]["resource_uri"])

			self._savePokemonData()

		else:
			self.buildStatus = False

	# this will get the sprite and set it
	def _setSprite(self, url):
		self._imagePath = os.path.join("resources", "pokemonSprites", self.name + ".png")
		if not os.path.isfile(self._imagePath):
			print "downloading pokemon image"
			r = requests.get(url)
			if r.status_code == 200:
				self.buildStatus = True
				resources = r.json()
				self._imageURL = resources["image"]

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

	# this will save the dowloaded pokemon data
	def _savePokemonData(self):
		pass