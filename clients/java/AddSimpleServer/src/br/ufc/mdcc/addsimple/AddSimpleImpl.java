package br.ufc.mdcc.addsimple;

import javax.annotation.Resource;
import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.ws.WebServiceContext;
import javax.xml.ws.handler.MessageContext;

import com.sun.net.httpserver.HttpExchange;

@WebService(endpointInterface = "br.ufc.mdcc.addsimple.AddSimple")

public class AddSimpleImpl implements AddSimple {
    @Resource 
    WebServiceContext wsContext;
	
	@WebMethod
	public String add_simple(String a, String b) {
		
		MessageContext msgx = wsContext.getMessageContext();
		HttpExchange exchange = (HttpExchange) msgx.get("com.sun.xml.internal.ws.http.exchange");
		System.out.println(exchange.getRemoteAddress().getAddress().getHostAddress());
	
		int A = Integer.parseInt(a);
		int B = Integer.parseInt(b);
		
		int C = A + B;
	
	    return "" + C;			
	}
}
