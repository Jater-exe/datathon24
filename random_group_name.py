import random

# List of adjectives
adjectives = [
    "Super", "Amazing", "Brilliant", "Epic", "Dynamic", "Legendary", "Mighty", "Fearless", 
    "Incredible", "Fantastic", "Unstoppable", "Powerful", "Invincible", "Creative", "Ultimate", 
    "Fierce", "Bold", "Visionary", "Resilient", "Majestic", "Radiant", "Heroic", "Majestic", 
    "Swift", "Revolutionary", "Pioneering", "Innovative", "Thunderous", "Elite", "Awesome", 
    "Supreme", "Champion", "Valiant", "Striking", "Electric", "Strategic", "Underdog", "Trailblazing"
]

# List of group names
group_names = [
    "Alpha Squad", "Beta Warriors", "Gamma Force", "Delta Knights", "Epsilon Pioneers",
    "Zeta Mavericks", "Eta Seekers", "Theta Guardians", "Iota Legends", "Kappa Titans",
    "Lambda Champions", "Mu Innovators", "Nu Explorers", "Xi Avengers", "Omicron Titans",
    "Pi Visionaries", "Rho Crusaders", "Sigma Shifters", "Tau Rebels", "Upsilon Mavericks",
    "Phi Pioneers", "Chi Revolutionaries", "Psi Dreamers", "Omega Guardians", "Alpha Crusaders",
    "Beta Legends", "Gamma Visionaries", "Delta Dreamers", "Epsilon Guardians", "Zeta Crusaders",
    "Eta Seekers", "Theta Shifters", "Iota Warriors", "Kappa Avengers", "Lambda Rebels",
    "Mu Explorers", "Nu Champions", "Xi Guardians", "Omicron Mavericks", "Pi Titans",
    "Rho Dreamers", "Sigma Avengers", "Tau Shifters", "Upsilon Seekers", "Phi Titans",
    "Chi Pioneers", "Psi Warriors", "Omega Seekers", "Apex Guardians", "Nexus Explorers",
    "Zenith Legends", "Vanguard Dreamers", "Ascend Pioneers", "Genesis Rebels", "Radiant Seekers",
    "Horizon Guardians", "Unity Avengers", "Momentum Champions", "Odyssey Shifters", "Pinnacle Titans",
    "Catalyst Warriors", "Horizon Titans", "Genesis Champions", "Summit Seekers", "Prism Dreamers",
    "Inferno Explorers", "Eclipse Guardians", "Vanguard Seekers", "Nova Legends", "Quantum Warriors",
    "Synthesis Champions", "Celestial Pioneers", "Stratosphere Seekers", "Luminous Avengers", "Cosmic Rebels",
    "Pioneer Legends", "Equinox Shifters", "Bouncy Programmers", "Solar Dreamers", "Neon Explorers",
    "Astral Warriors", "Skyline Seekers", "Zenith Guardians", "Ember Legends", "Nebula Titans",
    "Elysium Explorers", "Stellar Seekers", "Celestial Titans", "Cosmos Dreamers", "Astral Seekers",
    "Stratos Explorers", "Vortex Legends", "Orion Titans", "Eclipse Shifters", "Nova Seekers",
    "Radiance Warriors", "Infinity Seekers", "Nebula Dreamers", "Lunar Guardians", "Starlight Champions",
    "Spectra Titans", "Meteor Seekers", "Vortex Avengers", "Zenith Pioneers", "Astronaut Legends"
]

class GroupNameGenerator:
    def __init__(self):
        self.used_combinations = set()

    def generate_unique_group_name(self):
        while True:
            adjective = random.choice(adjectives)
            group_name = random.choice(group_names)
            
            combined_name = f"{adjective} {group_name}"
            
            if combined_name not in self.used_combinations:
                self.used_combinations.add(combined_name)  
                return combined_name

generator = GroupNameGenerator()
unique_group_name = generator.generate_unique_group_name()

print(f"Unique Group Name: {unique_group_name}")
