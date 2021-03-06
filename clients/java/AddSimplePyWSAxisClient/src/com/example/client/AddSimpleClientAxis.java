package com.example.client;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;

import br.ufc.mdcc.addsimple.AddSimpleDocument;
import br.ufc.mdcc.addsimple.AddSimpleDocument.AddSimple;
import br.ufc.mdcc.addsimple.AddSimpleImplServiceStub;
import br.ufc.mdcc.addsimple.AddSimpleResponseDocument;
import br.ufc.mdcc.addsimple.impl.AddSimpleDocumentImpl;

public class AddSimpleClientAxis {

	public static void main(String[] args) {
		try {
			// TestServiceStub stub = new
			// TestServiceStub("http://localhost:8000/api/");
			AddSimpleImplServiceStub stub = new AddSimpleImplServiceStub(
					"http://127.0.0.1:8080/axis2/services/CoreServices");

			// / AddTripleDocument request =
			// AddTripleDocument.Factory.newInstance();
			AddSimpleDocument request = AddSimpleDocument.Factory.newInstance();

			// AddTripleDocument.AddTriple data = request.addNewAddTriple();
			AddSimple data = request.addNewAddSimple();

			// data.setA("1");
			// data.setB("2");
			// data.setC("3");
			data.setArg0("1");
			data.setArg1("2");

			// AddTripleResultDocument response = stub.add_triple(request);
			AddSimpleResponseDocument response = stub.add_simple(request);

			// System.out.println(response.getAddTripleResult());
			System.out.println(response.getAddSimpleResponse().getReturn()	);
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
