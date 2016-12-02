package br.ufc.mdcc.hpcshelf.backendservices.pyws.client;

import java.net.MalformedURLException;
import java.net.URL;

import br.ufc.mdcc.hpcshelf.backendservices.pyws.BackEndPortType;
import br.ufc.mdcc.hpcshelf.backendservices.pyws.BackEndServicePyWS;
import br.ufc.mdcc.hpcshelf.backendservices.pyws.Error_Exception;

public class BackEndServicePyWSClient {
	private BackEndServicePyWS service;
	private BackEndPortType port;
	
	public BackEndServicePyWSClient(String endpoint){
		try {
			service = new BackEndServicePyWS(new URL(endpoint));
			port = service.getBackEndPort();
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public String deployContractCallback(String profileId, String coreSessionId, String remoteIP) {
		try {
			return port.deployContractCallback(profileId, coreSessionId, remoteIP);
		} catch (Error_Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public String destroyPlatform(String coreSessionId) {
		try {
			return port.destroyPlatform(coreSessionId);
		} catch (Error_Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
}
