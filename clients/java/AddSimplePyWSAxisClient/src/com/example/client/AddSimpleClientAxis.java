package com.example.client;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;

import com.example.Error;
import com.example.TestServiceStub;
import com.example.types.AddTripleDocument;
import com.example.types.AddTripleResultDocument;

public class AddSimpleClientAxis {

	public static void main(String[] args) {
		try {
			TestServiceStub stub = new TestServiceStub("http://localhost:8000/api/");

			AddTripleDocument request = AddTripleDocument.Factory.newInstance();
			AddTripleDocument.AddTriple data = request.addNewAddTriple();
			
			data.setA("1");
			data.setB("2");
			data.setC("3");
			
			AddTripleResultDocument response = stub.add_triple(request);
			
			System.out.println(response.getAddTripleResult());
		} catch (AxisFault e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (RemoteException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Error e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
