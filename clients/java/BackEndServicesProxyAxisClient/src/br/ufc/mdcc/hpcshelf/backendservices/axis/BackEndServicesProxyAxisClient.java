package br.ufc.mdcc.hpcshelf.backendservices.axis;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;

import br.ufc.mdcc.hpcshelf.backendservices.proxy.BackEndServicesImplServiceStub;
import br.ufc.mdcc.hpcshelf.backendservices.proxy.DeployContractCallbackDocument;
import br.ufc.mdcc.hpcshelf.backendservices.proxy.DeployContractCallbackDocument.DeployContractCallback;
import br.ufc.mdcc.hpcshelf.backendservices.proxy.DeployContractCallbackResponseDocument;

public class BackEndServicesProxyAxisClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			BackEndServicesImplServiceStub stub = new BackEndServicesImplServiceStub(args[0]);
			
			DeployContractCallbackDocument request = DeployContractCallbackDocument.Factory.newInstance();
			
			DeployContractCallback data = request.addNewDeployContractCallback();
			
			data.setArg0("321");
			data.setArg1("1234");
			
			DeployContractCallbackResponseDocument response = stub.deployContractCallback(request);
			System.out.println(response.getDeployContractCallbackResponse().getReturn());
		} catch (AxisFault e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (RemoteException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
