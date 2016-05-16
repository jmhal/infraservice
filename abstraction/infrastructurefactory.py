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
        infrastructure_type = self.profiles['infrastructure']['type']
        infrastructure_abstraction_module = importlib.import_module("abstraction." + infrastructure_type.lower())
        # the properties from the infrastructure must go here.
        infrastructure_abstraction = getattr(infrastructure_abstraction_module, infrastructure_type)

        profile_type = self.profiles['infrastructure']['profile_type']
        profile_implementor_module = importlib.import_module("implementor." + profile_type.lower())
        # the properties from the profile must go here
        profile_implementor = getattr(profile_implementor_module, profile_type)

        i = infrastructure_abstraction(profile_implementor)
        return i

def main():
    factory = InfrastructureFactory("/home/jmhal/repositorios/infrastructureservice/profiles/profiles_cloud.yaml")
    print factory.get_infrastructure()


if __name__ == "__main__":
    main()
