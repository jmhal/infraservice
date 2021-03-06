package com.example.client;

import java.net.MalformedURLException;
import java.net.URL;

import com.example.Error;
import com.example.TestPortType;
import com.example.TestService;

public class AddSimpleClientJAXWS {
	public static void main(String[] args) {
		try {
			TestService service = new TestService(new URL("http://localhost:8000/api/wsdl"));
			TestPortType port = service.getTestPort();
			
			System.out.println(port.addTriple("1", "2", "3"));
		} catch (Error e) {
			e.printStackTrace();
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
