package br.ufc.mdcc.hpcshelf.backend;

import javax.xml.ws.Endpoint;

public class BackEndServicesPublisher {

	public static void main(String[] args) {
		Endpoint.publish("http://" + args[0] + ":8080/BackEndServices", new BackEndServicesImpl());
	}
}