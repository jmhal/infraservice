package br.ufc.mdcc.hpcshelf.backend;

import javax.annotation.Resource;
import javax.jws.WebService;
import javax.xml.ws.WebServiceContext;
import javax.xml.ws.handler.MessageContext;

import com.sun.net.httpserver.HttpExchange;

@WebService(endpointInterface = "br.ufc.mdcc.hpcshelf.backend.BackEndServices")

public class BackEndServicesImpl implements BackEndServices {
	@Resource 
    WebServiceContext wsContext;

	@Override
	public String deployContractCallback(String profileId, String coreSessionId) {
		MessageContext msgx = wsContext.getMessageContext();
		HttpExchange exchange = (HttpExchange) msgx.get("com.sun.xml.internal.ws.http.exchange");
		String remote_ip = exchange.getRemoteAddress().getAddress().getHostAddress();
		
		// Call Local Python Web Service
		
		return null;
	}

	@Override
	public String destroyPlatform(String coreSessionId) {
		
		// Call Local Python Web Service
		
		return null;
	}

}
