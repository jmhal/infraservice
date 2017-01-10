package br.ufc.mdcc.hpcshelf.backendservices.proxy;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

@WebService
@SOAPBinding(style = Style.RPC)
public interface BackEndServices {
	@WebMethod
	String deployContractCallback(String profileId, String coreSessionId);
	
	@WebMethod
	String destroyPlatform(String coreSessionId);
}
