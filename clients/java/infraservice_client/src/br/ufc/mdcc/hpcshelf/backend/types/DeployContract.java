
package br.ufc.mdcc.hpcshelf.backend.types;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Classe Java de anonymous complex type.
 * 
 * <p>O seguinte fragmento do esquema especifica o conteúdo esperado contido dentro desta classe.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="contract" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "contract"
})
@XmlRootElement(name = "deploy_contract")
public class DeployContract {

    @XmlElement(required = true, nillable = true)
    protected String contract;

    /**
     * Obtém o valor da propriedade contract.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getContract() {
        return contract;
    }

    /**
     * Define o valor da propriedade contract.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setContract(String value) {
        this.contract = value;
    }

}
