"""
Chapitre 11.3

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import Character, Weapon


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	# TODO: __init__
	def __init__(self, nom, power, mp_cost, min_level) -> None:
		self.__name = nom
		self.power = power
		self.mp_cost = mp_cost
		self.min_level = min_level

	@property 
	
	def name(self):
		return self.__name
		

# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician(Character):
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend 

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param max_mp: MP maximum
	:param attack: Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""

	def __init__(self, name, max_hp, max_mp, attack, magic_attack, defense, level):
		# TODO: Initialiser les attributs de Character
		# TODO: Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		self.__name = name
		self.max_hp = max_hp
		self.max_mp = max_mp
		self.attack = attack
		self.magic_attack = magic_attack
		self.defense = defense
		self.level = level
		self.hp = max_hp
		self.mp = max_mp
		self.spell = None
		self.using_magic = False
		

	@property
	def mp(self):
		return self.Mp

	@mp.setter
	def mp(self, val):
		return (self.mp - val)

	@property 
	def spell(self):
		return self.spell

	# TODO: Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.
	@spell.setter
	def spell(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.spell = val
	# TODO: Surcharger la méthode `compute_damage` 
	def compute_damage(self, other):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
		if self.using_magic :
			self.mp -= Spell.mp_cost
			# Soustraire à son MP le coût du sort
			# Retourner le résultat du calcul de dégâts magiques
			dmg = ((2*self.level)/5) #compléter fonction
		# Sinon
			# Retourner le résultat du calcul de dégâts physiques
		pass

	def will_use_spell(self):
		pass

	def _compute_magical_damage(self, other):
		pass

	def _compute_physical_damage(self, other):
		# TODO: Calculer le dommage physique exactement de la même façon que dans `Character`
		pass

