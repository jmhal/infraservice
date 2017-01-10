package br.ufc.mdcc.addsimple;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

@WebService
@SOAPBinding(style = Style.RPC)
public interface AddSimple {
	@WebMethod
	String add_simple(String a, String b);

}
