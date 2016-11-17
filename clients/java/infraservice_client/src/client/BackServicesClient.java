package client;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

import br.ufc.mdcc.hpcshelf.backend.BackEndPortType;
import br.ufc.mdcc.hpcshelf.backend.BackEndService;
import br.ufc.mdcc.hpcshelf.backend.Error;
import br.ufc.mdcc.hpcshelf.backend.types.ProfilesIds;
import br.ufc.mdcc.hpcshelf.backend.types.ProfilesIdsList;


public class BackServicesClient {
	public static void main(String[] args) {
		
		try {
			String backEndServicesURL = "http://" + args[0] + ":8000/backendservices/wsdl";
			System.out.println(backEndServicesURL);
			BackEndService service = new BackEndService(new URL(backEndServicesURL));
			BackEndPortType port = service.getBackEndPort();
			
			System.out.println("Available Profiles:");
			ProfilesIdsList profileList = port.availableProfiles();
			List<ProfilesIds> item = profileList.getItem();
			for (ProfilesIds profilesIds : item) {
				System.out.println(profilesIds.getProfileId() + ":" + profilesIds.getProfileName());
			}
			
			System.out.println("Creating Profile: 0, Session ID: 104");
			String profile0ID = port.deployContractCallback("0", "104");
			
			System.out.println("Creating Profile: 1, Session ID: 105");
			String profile1ID = port.deployContractCallback("1", "105");
			
			String status0 = port.platformDeploymentStatus(profile0ID);
			String status1 = port.platformDeploymentStatus(profile1ID);
			while ( !status0.equals("CREATED") && !status1.equals("CREATED"))
			{
				System.out.println("Status 0:" + status0);
				System.out.println("Status 1:" + status1);
				Thread.sleep(15000);
				status0 = port.platformDeploymentStatus(profile0ID);
				status1 = port.platformDeploymentStatus(profile1ID);
			}
			
			System.out.println("Destroying Profile: 0, Session ID: 104");
			port.destroyPlatform(profile0ID);
			System.out.println("Destroying Profile: 1, Session ID: 105");
			port.destroyPlatform(profile1ID);
		} catch (MalformedURLException e) {

			e.printStackTrace();
		} catch (Error e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
