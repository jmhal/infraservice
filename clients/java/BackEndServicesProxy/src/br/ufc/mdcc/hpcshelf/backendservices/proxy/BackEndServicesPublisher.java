package br.ufc.mdcc.hpcshelf.backendservices.proxy;

import javax.xml.ws.Endpoint;

public class BackEndServicesPublisher {

	public static void main(String[] args) {
		String externalEndpoint = args[0];  // "http://200.19.177.89:8000/BackEndServices" 
		String localPyWSEndpoint = args[1]; // "http://200.19.177.89:8001/backendservices"
		Endpoint.publish(externalEndpoint, new BackEndServicesImpl(localPyWSEndpoint));
	}
}
