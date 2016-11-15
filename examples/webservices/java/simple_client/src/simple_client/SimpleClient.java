package simple_client;

import java.net.MalformedURLException;
import java.net.URL;

// import javax.xml.ws.WebServiceRef;


import com.example.Error;
import com.example.TestPortType;
import com.example.TestService;

public class SimpleClient {
	public static void main(String[] args) {
		
		try {
			TestService service = new TestService(new URL("http://192.168.1.110:8000/api/wsdl"));
			TestPortType port = service.getTestPort();	
			String simple = port.addSimple("João", "Marcelo");
			String triple = port.addTriple("Uchôa", "de", "Alencar");
			System.out.println(simple);
			System.out.println(triple);
			
		} catch (Error e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
