using System;
using System.Collections;

namespace BackEndServicesClient
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			BackEndService service = new BackEndService ();

			profiles_ids [] profiles = service.available_profiles ();
			Console.WriteLine ("Perfis disponíveis:");
			for (int i = 0; i < profiles.Length; i++) {
				Console.WriteLine (profiles [i].profile_name + ": " + profiles[i].profile_id);
			}

			ArrayList endpointList = new ArrayList ();

			for (int i = 0; i < 5; i++) {
				Console.WriteLine ("Fazendo Deploy do Perfil 1985:");
				String endpoint = service.deploy ("1985");
				endpointList.Add (endpoint);
				Console.WriteLine ("Endpoint da Plataforma:" + endpoint);
			}

			Console.WriteLine ("Pressione qualquer tecla para continuar...");
			Console.Read ();

			foreach (String endpoint in endpointList) {
				Console.WriteLine ("Destruindo Plataforma com endpoint: " + endpoint);
				service.destroy (endpoint);
			}
	   	}
	}
}
