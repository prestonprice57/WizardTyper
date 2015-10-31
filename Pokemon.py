import Entities
import requests
import shutil
import os.path

class Pokemon(Entities.Entity):

	def __init__(self, pokemonID):
		super(Pokemon, self).__init__()

		self._BASE_IMAGE_PATH = os.path.join("resources", "pokemonSprites")

		# the followin are stats that need to be found in order for it to be a valid pokemon
		self.pokemonID = pokemonID
		self.name = None
		self.stats.hp = None
		self.stats.magicPower = None
		self.stats.magicResistance = None
		self.image = None
		self.buildStatus = False

		# if the data file already exists then use it
		self._pokemonDataPath = "pokemon" + str(pokemonID) + ".pokedat"
		self._pokemonDataPath = os.path.join("resources", "pokemonData", self._pokemonDataPath)
		if os.path.isfile(self._pokemonDataPath):
			lines = list(open(self._pokemonDataPath))
			for line in lines:
				dataArray = line.split(',')
				if dataArray[0] == "name":
					self.name = str(dataArray[1])
				elif dataArray[0] == "hp":
					self.stats.hp = int(dataArray[1])
				elif dataArray[0] == "resist":
					self.stats.magicResistance = int(dataArray[1])
				elif dataArray[0] == "power":
					self.stats.magicPower = int(dataArray[1])
				elif dataArray[0] == "image":
					self.image = str(dataArray[1])
					self._setSprite(os.path.join(self._BASE_IMAGE_PATH, self.image))
		else:
			# download the files
			self._downloadPokemon(pokemonID)
			self._savePokemonData(self._pokemonDataPath)

		self._validateBuild()
		
	def _downloadPokemon(self, pokemonID):
		# download the pokemon
		print "downloading pokemon data"
		self._BASEURL = "http://pokeapi.co"
		r = requests.get(self._BASEURL + '/api/v1/pokemon/' + str(pokemonID) + "/")

		if r.status_code == 200:
   			json = r.json()
			self.name = json["name"]
			self.image = self.name + ".png"
			self.stats.hp = json["hp"]
			
			# magic power and magic resistance will be the max power and resistance of the pokemon
			if json["attack"] > json["sp_atk"]:
				self.stats.magicPower = json["attack"]
			else:
				self.stats.magicPower = json["sp_atk"]
			if json["defense"] > json["sp_def"]:
				self.stats.magicResistance = json["defense"]
			else:
				self.stats.magicResistance = json["sp_def"]

			# now we need to set the sprite
			imagePath = os.path.join(self._BASE_IMAGE_PATH, self.image)
			resourceURL = self._BASEURL + json["sprites"][0]["resource_uri"]
			self._downloadSprite(resourceURL, imagePath)
			self._setSprite(imagePath)


	# this will get the sprite and set it
	def _downloadSprite(self, resourceURL, imagePath):
		if not os.path.isfile(imagePath):
			print "downloading pokemon image"
			r = requests.get(resourceURL)
			if r.status_code == 200:
				resources = r.json()
				imageURL = resources["image"]

				# download sprite
				response = requests.get(self._BASEURL + imageURL, stream=True)
				if response.status_code == 200:
					with open(imagePath, 'wb') as out_file:
						shutil.copyfileobj(response.raw, out_file)
						del response

	def _setSprite(self, spritePath):
		pass

	# this will save the dowloaded pokemon data
	def _savePokemonData(self, filename):
		with open(filename, 'w') as f:
			f.write("name," + self.name + '\n')
			f.write("hp," + str(self.stats.hp) + '\n')
			f.write("power," + str(self.stats.magicPower) + '\n')
			f.write("resist," + str(self.stats.magicResistance) + '\n')
			f.write("image," + self.name + ".png\n")
		print "pokemon data saved"

	# this validates the pokemon build status
	def _validateBuild(self):
		if self.name != None and self.stats.hp != None and self.stats.magicPower != None and self.stats.magicResistance != None:
			self.buildStatus = True
		else:
			self.buildStatus = False