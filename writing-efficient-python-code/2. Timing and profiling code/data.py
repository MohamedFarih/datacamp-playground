import array as arr

wts = [441.0,
 65.0,
 90.0,
 441.0,
 122.0,
 88.0,
 61.0,
 81.0,
 104.0,
 108.0,
 90.0,
 90.0,
 72.0,
 169.0,
 173.0,
 101.0,
 68.0,
 57.0,
 54.0,
 83.0,
 90.0,
 122.0,
 86.0,
 358.0,
 135.0,
 106.0,
 146.0,
 63.0,
 68.0,
 57.0,
 98.0,
 270.0,
 59.0,
 50.0,
 101.0,
 68.0,
 54.0,
 81.0,
 63.0,
 67.0,
 180.0,
 77.0,
 54.0,
 57.0,
 52.0,
 61.0,
 95.0,
 79.0,
 133.0,
 63.0,
 181.0,
 68.0,
 216.0,
 135.0,
 71.0,
 54.0,
 124.0,
 155.0,
 113.0,
 95.0,
 58.0,
 54.0,
 86.0,
 90.0,
 52.0,
 92.0,
 90.0,
 59.0,
 61.0,
 104.0,
 86.0,
 88.0,
 97.0,
 68.0,
 56.0,
 77.0,
 230.0,
 495.0,
 86.0,
 55.0,
 97.0,
 110.0,
 135.0,
 61.0,
 99.0,
 52.0,
 90.0,
 59.0,
 158.0,
 74.0,
 81.0,
 108.0,
 90.0,
 116.0,
 108.0,
 74.0,
 74.0,
 86.0,
 61.0,
 61.0,
 62.0,
 97.0,
 63.0,
 81.0,
 50.0,
 55.0,
 54.0,
 86.0,
 170.0,
 70.0,
 78.0,
 225.0,
 67.0,
 79.0,
 99.0,
 104.0,
 50.0,
 173.0,
 88.0,
 68.0,
 52.0,
 90.0,
 81.0,
 817.0,
 56.0,
 135.0,
 27.0,
 52.0,
 90.0,
 95.0,
 91.0,
 178.0,
 101.0,
 95.0,
 383.0,
 90.0,
 171.0,
 187.0,
 132.0,
 89.0,
 110.0,
 81.0,
 54.0,
 63.0,
 412.0,
 104.0,
 306.0,
 56.0,
 74.0,
 59.0,
 80.0,
 65.0,
 57.0,
 203.0,
 95.0,
 106.0,
 88.0,
 96.0,
 108.0,
 50.0,
 18.0,
 56.0,
 99.0,
 56.0,
 91.0,
 81.0,
 88.0,
 86.0,
 52.0,
 81.0,
 45.0,
 92.0,
 104.0,
 167.0,
 16.0,
 81.0,
 77.0,
 86.0,
 99.0,
 630.0,
 268.0,
 50.0,
 62.0,
 90.0,
 270.0,
 115.0,
 79.0,
 88.0,
 83.0,
 77.0,
 88.0,
 79.0,
 4.0,
 95.0,
 90.0,
 79.0,
 63.0,
 79.0,
 89.0,
 104.0,
 57.0,
 61.0,
 88.0,
 54.0,
 65.0,
 81.0,
 225.0,
 158.0,
 61.0,
 81.0,
 146.0,
 83.0,
 48.0,
 18.0,
 630.0,
 77.0,
 59.0,
 58.0,
 77.0,
 119.0,
 207.0,
 65.0,
 65.0,
 81.0,
 54.0,
 79.0,
 191.0,
 79.0,
 14.0,
 77.0,
 52.0,
 55.0,
 56.0,
 113.0,
 90.0,
 88.0,
 86.0,
 49.0,
 52.0,
 855.0,
 81.0,
 104.0,
 72.0,
 356.0,
 324.0,
 203.0,
 97.0,
 99.0,
 106.0,
 18.0,
 79.0,
 58.0,
 63.0,
 59.0,
 95.0,
 54.0,
 65.0,
 95.0,
 360.0,
 230.0,
 288.0,
 236.0,
 36.0,
 191.0,
 77.0,
 79.0,
 383.0,
 86.0,
 225.0,
 90.0,
 97.0,
 52.0,
 135.0,
 56.0,
 81.0,
 110.0,
 72.0,
 59.0,
 54.0,
 140.0,
 72.0,
 90.0,
 90.0,
 86.0,
 77.0,
 101.0,
 61.0,
 81.0,
 86.0,
 128.0,
 61.0,
 338.0,
 248.0,
 90.0,
 101.0,
 59.0,
 79.0,
 79.0,
 72.0,
 70.0,
 158.0,
 61.0,
 70.0,
 79.0,
 54.0,
 125.0,
 85.0,
 101.0,
 54.0,
 83.0,
 99.0,
 88.0,
 79.0,
 83.0,
 86.0,
 293.0,
 191.0,
 65.0,
 69.0,
 405.0,
 59.0,
 117.0,
 89.0,
 79.0,
 54.0,
 52.0,
 87.0,
 80.0,
 55.0,
 50.0,
 52.0,
 81.0,
 234.0,
 86.0,
 81.0,
 70.0,
 90.0,
 74.0,
 68.0,
 83.0,
 79.0,
 56.0,
 97.0,
 50.0,
 70.0,
 117.0,
 83.0,
 81.0,
 630.0,
 56.0,
 108.0,
 146.0,
 320.0,
 85.0,
 72.0,
 79.0,
 101.0,
 56.0,
 38.0,
 25.0,
 54.0,
 104.0,
 63.0,
 171.0,
 61.0,
 203.0,
 900.0,
 63.0,
 74.0,
 113.0,
 59.0,
 310.0,
 87.0,
 149.0,
 54.0,
 50.0,
 79.0,
 88.0,
 315.0,
 153.0,
 79.0,
 52.0,
 191.0,
 101.0,
 50.0,
 92.0,
 72.0,
 52.0,
 180.0,
 49.0,
 437.0,
 65.0,
 113.0,
 405.0,
 54.0,
 56.0,
 74.0,
 59.0,
 55.0,
 58.0,
 81.0,
 83.0,
 79.0,
 71.0,
 62.0,
 63.0,
 131.0,
 91.0,
 57.0,
 77.0,
 68.0,
 77.0,
 54.0,
 101.0,
 47.0,
 74.0,
 146.0,
 99.0,
 54.0,
 443.0,
 101.0,
 225.0,
 288.0,
 143.0,
 101.0,
 74.0,
 288.0,
 158.0,
 203.0,
 81.0,
 54.0,
 76.0,
 97.0,
 81.0,
 59.0,
 86.0,
 82.0,
 105.0,
 331.0,
 58.0,
 54.0,
 56.0,
 214.0,
 79.0,
 73.0,
 117.0,
 50.0,
 334.0,
 52.0,
 71.0,
 54.0,
 41.0,
 135.0,
 135.0,
 63.0,
 79.0,
 162.0,
 95.0,
 54.0,
 108.0,
 67.0,
 158.0,
 50.0,
 65.0,
 117.0,
 39.0,
 473.0,
 135.0,
 51.0,
 171.0,
 74.0,
 117.0,
 50.0,
 61.0,
 95.0,
 83.0,
 52.0,
 17.0,
 57.0,
 81.0]

heroes = ['A-Bomb',
 'Abe Sapien',
 'Abin Sur',
 'Abomination',
 'Absorbing Man',
 'Adam Strange',
 'Agent 13',
 'Agent Bob',
 'Agent Zero',
 'Air-Walker',
 'Ajax',
 'Alan Scott',
 'Alfred Pennyworth',
 'Alien',
 'Amazo',
 'Ammo',
 'Angel',
 'Angel Dust',
 'Angel Salvadore',
 'Animal Man',
 'Annihilus',
 'Ant-Man',
 'Ant-Man II',
 'Anti-Venom',
 'Apocalypse',
 'Aqualad',
 'Aquaman',
 'Arachne',
 'Archangel',
 'Arclight',
 'Ardina',
 'Ares',
 'Ariel',
 'Armor',
 'Atlas',
 'Atom',
 'Atom Girl',
 'Atom II',
 'Aurora',
 'Azazel',
 'Bane',
 'Banshee',
 'Bantam',
 'Batgirl',
 'Batgirl IV',
 'Batgirl VI',
 'Batman',
 'Batman II',
 'Battlestar',
 'Beak',
 'Beast',
 'Beast Boy',
 'Beta Ray Bill',
 'Big Barda',
 'Big Man',
 'Binary',
 'Bishop',
 'Bizarro',
 'Black Adam',
 'Black Bolt',
 'Black Canary',
 'Black Cat',
 'Black Knight III',
 'Black Lightning',
 'Black Mamba',
 'Black Manta',
 'Black Panther',
 'Black Widow',
 'Black Widow II',
 'Blackout',
 'Blackwing',
 'Blackwulf',
 'Blade',
 'Bling!',
 'Blink',
 'Blizzard II',
 'Blob',
 'Bloodaxe',
 'Blue Beetle II',
 'Boom-Boom',
 'Booster Gold',
 'Box III',
 'Brainiac',
 'Brainiac 5',
 'Brother Voodoo',
 'Buffy',
 'Bullseye',
 'Bumblebee',
 'Cable',
 'Callisto',
 'Cannonball',
 'Captain America',
 'Captain Atom',
 'Captain Britain',
 'Captain Mar-vell',
 'Captain Marvel',
 'Captain Marvel II',
 'Carnage',
 'Cat',
 'Catwoman',
 'Cecilia Reyes',
 'Century',
 'Chamber',
 'Changeling',
 'Cheetah',
 'Cheetah II',
 'Cheetah III',
 'Chromos',
 'Citizen Steel',
 'Cloak',
 'Clock King',
 'Colossus',
 'Copycat',
 'Corsair',
 'Cottonmouth',
 'Crimson Dynamo',
 'Crystal',
 'Cyborg',
 'Cyclops',
 'Cypher',
 'Dagger',
 'Daredevil',
 'Darkhawk',
 'Darkseid',
 'Darkstar',
 'Darth Vader',
 'Dash',
 'Dazzler',
 'Deadman',
 'Deadpool',
 'Deadshot',
 'Deathlok',
 'Deathstroke',
 'Demogoblin',
 'Destroyer',
 'Diamondback',
 'Doc Samson',
 'Doctor Doom',
 'Doctor Doom II',
 'Doctor Fate',
 'Doctor Octopus',
 'Doctor Strange',
 'Domino',
 'Donna Troy',
 'Doomsday',
 'Doppelganger',
 'Drax the Destroyer',
 'Elastigirl',
 'Electro',
 'Elektra',
 'Elongated Man',
 'Emma Frost',
 'Enchantress',
 'Etrigan',
 'Evil Deadpool',
 'Evilhawk',
 'Exodus',
 'Fabian Cortez',
 'Falcon',
 'Feral',
 'Fin Fang Foom',
 'Firebird',
 'Firelord',
 'Firestar',
 'Firestorm',
 'Flash',
 'Flash II',
 'Flash III',
 'Flash IV',
 'Forge',
 'Franklin Richards',
 'Franklin Storm',
 'Frenzy',
 'Frigga',
 'Galactus',
 'Gambit',
 'Gamora',
 'Genesis',
 'Ghost Rider',
 'Giganta',
 'Gladiator',
 'Goblin Queen',
 'Goku',
 'Goliath IV',
 'Gorilla Grodd',
 'Granny Goodness',
 'Gravity',
 'Green Arrow',
 'Green Goblin',
 'Green Goblin II',
 'Green Goblin III',
 'Green Goblin IV',
 'Groot',
 'Guy Gardner',
 'Hal Jordan',
 'Han Solo',
 'Harley Quinn',
 'Havok',
 'Hawk',
 'Hawkeye',
 'Hawkeye II',
 'Hawkgirl',
 'Hawkman',
 'Hawkwoman',
 'Hawkwoman III',
 'Heat Wave',
 'Hela',
 'Hellboy',
 'Hellcat',
 'Hellstorm',
 'Hercules',
 'Hobgoblin',
 'Hope Summers',
 'Howard the Duck',
 'Hulk',
 'Human Torch',
 'Huntress',
 'Husk',
 'Hybrid',
 'Hydro-Man',
 'Hyperion',
 'Iceman',
 'Impulse',
 'Ink',
 'Invisible Woman',
 'Iron Fist',
 'Iron Man',
 'Jack of Hearts',
 'Jack-Jack',
 'James T. Kirk',
 'Jean Grey',
 'Jennifer Kale',
 'Jessica Jones',
 'Jigsaw',
 'John Stewart',
 'John Wraith',
 'Joker',
 'Jolt',
 'Jubilee',
 'Juggernaut',
 'Justice',
 'Kang',
 'Karate Kid',
 'Killer Croc',
 'Kilowog',
 'Kingpin',
 'Klaw',
 'Kraven II',
 'Kraven the Hunter',
 'Krypto',
 'Kyle Rayner',
 'Lady Deathstrike',
 'Leader',
 'Legion',
 'Lex Luthor',
 'Light Lass',
 'Lightning Lad',
 'Lightning Lord',
 'Living Brain',
 'Lizard',
 'Lobo',
 'Loki',
 'Longshot',
 'Luke Cage',
 'Luke Skywalker',
 'Mach-IV',
 'Machine Man',
 'Magneto',
 'Man-Thing',
 'Man-Wolf',
 'Mandarin',
 'Mantis',
 'Martian Manhunter',
 'Marvel Girl',
 'Master Brood',
 'Maverick',
 'Maxima',
 'Medusa',
 'Meltdown',
 'Mephisto',
 'Mera',
 'Metallo',
 'Metamorpho',
 'Metron',
 'Micro Lad',
 'Mimic',
 'Miss Martian',
 'Mister Fantastic',
 'Mister Freeze',
 'Mister Sinister',
 'Mockingbird',
 'MODOK',
 'Molten Man',
 'Monarch',
 'Moon Knight',
 'Moonstone',
 'Morlun',
 'Morph',
 'Moses Magnum',
 'Mr Immortal',
 'Mr Incredible',
 'Ms Marvel II',
 'Multiple Man',
 'Mysterio',
 'Mystique',
 'Namor',
 'Namora',
 'Namorita',
 'Naruto Uzumaki',
 'Nebula',
 'Nick Fury',
 'Nightcrawler',
 'Nightwing',
 'Northstar',
 'Nova',
 'Odin',
 'Omega Red',
 'Omniscient',
 'One Punch Man',
 'Onslaught',
 'Oracle',
 'Paul Blart',
 'Penance II',
 'Penguin',
 'Phantom Girl',
 'Phoenix',
 'Plantman',
 'Plastic Man',
 'Plastique',
 'Poison Ivy',
 'Polaris',
 'Power Girl',
 'Predator',
 'Professor X',
 'Professor Zoom',
 'Psylocke',
 'Punisher',
 'Purple Man',
 'Pyro',
 'Question',
 'Quicksilver',
 'Quill',
 "Ra's Al Ghul",
 'Raven',
 'Ray',
 'Razor-Fist II',
 'Red Arrow',
 'Red Hood',
 'Red Hulk',
 'Red Robin',
 'Red Skull',
 'Red Tornado',
 'Rhino',
 'Rick Flag',
 'Ripcord',
 'Robin',
 'Robin II',
 'Robin III',
 'Robin V',
 'Rocket Raccoon',
 'Rogue',
 'Ronin',
 'Rorschach',
 'Sabretooth',
 'Sage',
 'Sandman',
 'Sasquatch',
 'Scarecrow',
 'Scarlet Spider',
 'Scarlet Spider II',
 'Scarlet Witch',
 'Scorpion',
 'Sentry',
 'Shadow King',
 'Shadow Lass',
 'Shadowcat',
 'Shang-Chi',
 'Shatterstar',
 'She-Hulk',
 'She-Thing',
 'Shocker',
 'Shriek',
 'Sif',
 'Silver Surfer',
 'Silverclaw',
 'Sinestro',
 'Siren',
 'Siryn',
 'Skaar',
 'Snowbird',
 'Solomon Grundy',
 'Songbird',
 'Space Ghost',
 'Spawn',
 'Spider-Girl',
 'Spider-Gwen',
 'Spider-Man',
 'Spider-Woman',
 'Spider-Woman III',
 'Spider-Woman IV',
 'Spock',
 'Spyke',
 'Star-Lord',
 'Starfire',
 'Stargirl',
 'Static',
 'Steel',
 'Steppenwolf',
 'Storm',
 'Sunspot',
 'Superboy',
 'Superboy-Prime',
 'Supergirl',
 'Superman',
 'Swarm',
 'Synch',
 'T-1000',
 'Taskmaster',
 'Tempest',
 'Thanos',
 'The Comedian',
 'Thing',
 'Thor',
 'Thor Girl',
 'Thunderbird',
 'Thunderbird III',
 'Thunderstrike',
 'Thundra',
 'Tiger Shark',
 'Tigra',
 'Tinkerer',
 'Toad',
 'Toxin',
 'Trickster',
 'Triplicate Girl',
 'Triton',
 'Two-Face',
 'Ultragirl',
 'Ultron',
 'Utgard-Loki',
 'Vagabond',
 'Valerie Hart',
 'Valkyrie',
 'Vanisher',
 'Vegeta',
 'Venom',
 'Venom II',
 'Venom III',
 'Vertigo II',
 'Vibe',
 'Vindicator',
 'Violet Parr',
 'Vision',
 'Vision II',
 'Vixen',
 'Vulture',
 'Walrus',
 'War Machine',
 'Warbird',
 'Warlock',
 'Warp',
 'Warpath',
 'Wasp',
 'White Queen',
 'Winter Soldier',
 'Wiz Kid',
 'Wolfsbane',
 'Wolverine',
 'Wonder Girl',
 'Wonder Man',
 'Wonder Woman',
 'Wyatt Wingfoot',
 'X-23',
 'X-Man',
 'Yellow Claw',
 'Yellowjacket',
 'Yellowjacket II',
 'Yoda',
 'Zatanna',
 'Zoom']

hts = [203. , 191. , 185. , 203. , 193. , 185. , 173. , 178. , 191. ,
       188. , 193. , 180. , 178. , 244. , 257. , 188. , 183. , 165. ,
       163. , 183. , 180. , 211. , 183. , 229. , 213. , 178. , 185. ,
       175. , 183. , 173. , 193. , 185. , 165. , 163. , 183. , 178. ,
       168. , 183. , 180. , 183. , 203. , 183. , 165. , 170. , 165. ,
       168. , 188. , 178. , 198. , 175. , 180. , 173. , 201. , 188. ,
       165. , 180. , 198. , 191. , 191. , 188. , 165. , 178. , 183. ,
       185. , 170. , 188. , 183. , 170. , 170. , 191. , 185. , 188. ,
       188. , 168. , 165. , 175. , 178. , 218. , 183. , 165. , 196. ,
       193. , 198. , 170. , 183. , 157. , 183. , 170. , 203. , 175. ,
       183. , 188. , 193. , 198. , 188. , 180. , 175. , 185. , 173. ,
       175. , 170. , 201. , 175. , 180. , 163. , 170. , 175. , 185. ,
       183. , 226. , 178. , 226. , 183. , 191. , 183. , 180. , 168. ,
       198. , 191. , 175. , 165. , 183. , 185. , 267. , 168. , 198. ,
       122. , 173. , 183. , 188. , 185. , 193. , 193. , 185. , 188. ,
       193. , 198. , 201. , 201. , 188. , 175. , 188. , 173. , 175. ,
       244. , 196. , 193. , 168. , 180. , 175. , 185. , 178. , 168. ,
       193. , 188. , 191. , 183. , 196. , 188. , 175. , 975. , 165. ,
       193. , 173. , 188. , 180. , 183. , 183. , 157. , 183. , 142. ,
       188. , 211. , 180. , 876. , 185. , 183. , 185. , 188. ,  62.5,
       198. , 168. , 175. , 183. , 198. , 178. , 178. , 188. , 180. ,
       178. , 183. , 178. , 701. , 188. , 188. , 183. , 170. , 183. ,
       185. , 191. , 165. , 175. , 185. , 175. , 170. , 180. , 213. ,
       259. , 173. , 185. , 196. , 180. , 168. ,  79. , 244. , 178. ,
       180. , 170. , 175. , 188. , 183. , 173. , 170. , 180. , 168. ,
       180. , 198. , 155. ,  71. , 178. , 168. , 168. , 170. , 188. ,
       185. , 183. , 196. , 165. , 165. , 287. , 178. , 191. , 173. ,
       244. , 234. , 201. , 188. , 191. , 183. ,  64. , 180. , 175. ,
       178. , 175. , 188. , 165. , 155. , 191. , 198. , 203. , 229. ,
       193. , 188. , 198. , 168. , 180. , 183. , 188. , 213. , 188. ,
       188. , 168. , 201. , 170. , 183. , 193. , 180. , 180. , 165. ,
       198. , 175. , 196. , 185. , 185. , 183. , 188. , 178. , 185. ,
       183. , 196. , 175. , 366. , 196. , 193. , 188. , 180. , 188. ,
       178. , 175. , 188. , 201. , 173. , 180. , 180. , 178. , 188. ,
       180. , 168. , 168. , 185. , 185. , 175. , 178. , 180. , 185. ,
       206. , 211. , 180. , 175. , 305. , 178. , 170. , 183. , 157. ,
       168. , 168. , 183. , 185. , 168. , 168. , 170. , 180. , 213. ,
       183. , 180. , 180. , 183. , 180. , 178. , 188. , 183. , 163. ,
       193. , 165. , 178. , 191. , 180. , 183. , 213. , 165. , 188. ,
       185. , 196. , 185. , 180. , 178. , 183. , 165. , 137. , 122. ,
       173. , 191. , 168. , 198. , 170. , 185. , 305. , 183. , 178. ,
       193. , 170. , 211. , 188. , 185. , 173. , 168. , 178. , 191. ,
       201. , 183. , 175. , 173. , 188. , 193. , 157. , 201. , 175. ,
       168. , 198. , 178. , 279. , 165. , 188. , 211. , 170. , 165. ,
       178. , 178. , 173. , 178. , 185. , 183. , 188. , 193. , 165. ,
       170. , 201. , 183. , 180. , 173. , 170. , 180. , 165. , 191. ,
       196. , 180. , 183. , 188. , 163. , 201. , 188. , 183. , 198. ,
       175. , 185. , 175. , 198. , 218. , 185. , 178. , 163. , 175. ,
       188. , 183. , 168. , 188. , 183. , 168. , 206. ,  15.2, 168. ,
       175. , 191. , 165. , 168. , 191. , 175. , 229. , 168. , 178. ,
       165. , 137. , 191. , 191. , 175. , 180. , 183. , 185. , 180. ,
       188. , 173. , 218. , 163. , 178. , 175. , 140. , 366. , 160. ,
       165. , 188. , 183. , 196. , 155. , 175. , 188. , 183. , 165. ,
        66. , 170. , 185.]

publishers = ['Marvel Comics',
 'Dark Horse Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Dark Horse Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Team Epic TV',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'George Lucas',
 'Dark Horse Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Shueisha',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'George Lucas',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Star Trek',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'George Lucas',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Team Epic TV',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Shueisha',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Team Epic TV',
 'Shueisha',
 'Marvel Comics',
 'DC Comics',
 'Sony Pictures',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Image Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Star Trek',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Team Epic TV',
 'Marvel Comics',
 'Marvel Comics',
 'Shueisha',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Dark Horse Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'DC Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'Marvel Comics',
 'George Lucas',
 'DC Comics',
 'DC Comics']
