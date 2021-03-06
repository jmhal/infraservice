
package br.ufc.mdcc.hpcshelf.backend;

import javax.xml.ws.WebFault;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.9-b130926.1035
 * Generated source version: 2.2
 * 
 */
@WebFault(name = "Error", targetNamespace = "http://www.mdcc.ufc.br/hpcshelf/backend/types/")
public class Error
    extends Exception
{

    /**
     * Java type that goes as soapenv:Fault detail element.
     * 
     */
    private br.ufc.mdcc.hpcshelf.backend.types.Error faultInfo;

    /**
     * 
     * @param faultInfo
     * @param message
     */
    public Error(String message, br.ufc.mdcc.hpcshelf.backend.types.Error faultInfo) {
        super(message);
        this.faultInfo = faultInfo;
    }

    /**
     * 
     * @param faultInfo
     * @param cause
     * @param message
     */
    public Error(String message, br.ufc.mdcc.hpcshelf.backend.types.Error faultInfo, Throwable cause) {
        super(message, cause);
        this.faultInfo = faultInfo;
    }

    /**
     * 
     * @return
     *     returns fault bean: br.ufc.mdcc.hpcshelf.backend.types.Error
     */
    public br.ufc.mdcc.hpcshelf.backend.types.Error getFaultInfo() {
        return faultInfo;
    }

}
