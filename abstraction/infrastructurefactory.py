"""
This class will load the profiles file and create the appropriate abstraction.
Don't mind it is a factory for abstract classes ;)
"""
import yaml
import importlib

class InfrastructureFactory:
    def __init__(self, profiles_file):
        self.profiles_file = profiles_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        return yaml.load(open(self.profiles_file,"r"))

    def get_profiles(self):
        return self.profiles['infrastructure']['profiles']

    def get_properties(self):
        return self.profiles['infrastructure']['properties']

    def get_infrastructure(self):
        """
        From the profiles file, create an infrastructure abstraction (type)
        with the corresponding profile implementor (profile_type).
        """
        infrastructure_type = self.profiles['infrastructure']['type']
        infrastructure_abstraction_module = importlib.import_module("abstraction." + infrastructure_type.lower())
        infrastructure_abstraction = getattr(infrastructure_abstraction_module, infrastructure_type)

        profile_type = self.profiles['infrastructure']['profile_type']
        properties = self.profiles['infrastructure']['properties']
        profiles = self.profiles['infrastructure']['profiles']
        profile_implementor_module = importlib.import_module("implementor." + profile_type.lower())
        profile_implementor = getattr(profile_implementor_module, profile_type)

        infrastructure = infrastructure_abstraction(profile_implementor(profiles, properties))
        return infrastructure

def main():
    factory = InfrastructureFactory("/home/jmhal/repositorios/infraservice/profiles/profiles_cluster.yaml")
    print factory.get_infrastructure()


if __name__ == "__main__":
    main()
