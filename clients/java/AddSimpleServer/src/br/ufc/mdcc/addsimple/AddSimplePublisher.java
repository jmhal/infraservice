package br.ufc.mdcc.addsimple;

import javax.xml.ws.Endpoint;

public class AddSimplePublisher {

	public static void main(String[] args) {
		Endpoint.publish("http://" + args[0] + ":8080/axis2/services/CoreServices", new AddSimpleImpl());
	}
}
