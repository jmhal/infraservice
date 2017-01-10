
package br.ufc.mdcc.hpcshelf.backendservices.pyws;

import javax.xml.ws.WebFault;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.9-b130926.1035
 * Generated source version: 2.2
 * 
 */
@WebFault(name = "Error", targetNamespace = "http://www.mdcc.ufc.br/hpcshelf/backend/types/")
public class Error_Exception
    extends Exception
{

    /**
     * Java type that goes as soapenv:Fault detail element.
     * 
     */
    private Error faultInfo;

    /**
     * 
     * @param faultInfo
     * @param message
     */
    public Error_Exception(String message, Error faultInfo) {
        super(message);
        this.faultInfo = faultInfo;
    }

    /**
     * 
     * @param faultInfo
     * @param cause
     * @param message
     */
    public Error_Exception(String message, Error faultInfo, Throwable cause) {
        super(message, cause);
        this.faultInfo = faultInfo;
    }

    /**
     * 
     * @return
     *     returns fault bean: br.ufc.mdcc.hpcshelf.backendservices.pywsclient.Error
     */
    public Error getFaultInfo() {
        return faultInfo;
    }

}
