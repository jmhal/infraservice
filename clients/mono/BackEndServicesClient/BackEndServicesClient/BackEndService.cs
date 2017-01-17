// ------------------------------------------------------------------------------
//  <autogenerated>
//      This code was generated by a tool.
//      Mono Runtime Version: 4.0.30319.17020
// 
//      Changes to this file may cause incorrect behavior and will be lost if 
//      the code is regenerated.
//  </autogenerated>
// ------------------------------------------------------------------------------

using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Web.Services;
using System.Web.Services.Protocols;
using System.Xml.Serialization;

// 
// This source code was auto-generated by Web Services Description Language Utility
//Mono Framework v4.0.30319.17020
//


/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Web.Services.WebServiceBindingAttribute(Name="BackEndBinding", Namespace="http://www.mdcc.ufc.br/hpcshelf/backend/")]
public partial class BackEndService : System.Web.Services.Protocols.SoapHttpClientProtocol {
    
    private System.Threading.SendOrPostCallback platform_deployment_statusOperationCompleted;
    
    private System.Threading.SendOrPostCallback destroy_platformOperationCompleted;
    
    private System.Threading.SendOrPostCallback deployOperationCompleted;
    
    private System.Threading.SendOrPostCallback available_profilesOperationCompleted;
    
    private System.Threading.SendOrPostCallback deploy_contractOperationCompleted;
    
    private System.Threading.SendOrPostCallback available_platformsOperationCompleted;
    
    private System.Threading.SendOrPostCallback deploy_contract_callbackOperationCompleted;
    
    private System.Threading.SendOrPostCallback get_platform_endpointOperationCompleted;
    
    private System.Threading.SendOrPostCallback destroyOperationCompleted;
    
    /// CodeRemarks
    public BackEndService() {
        this.Url = "http://200.19.177.89:8001/backendservices/";
    }
    
    /// CodeRemarks
    public event platform_deployment_statusCompletedEventHandler platform_deployment_statusCompleted;
    
    /// CodeRemarks
    public event destroy_platformCompletedEventHandler destroy_platformCompleted;
    
    /// CodeRemarks
    public event deployCompletedEventHandler deployCompleted;
    
    /// CodeRemarks
    public event available_profilesCompletedEventHandler available_profilesCompleted;
    
    /// CodeRemarks
    public event deploy_contractCompletedEventHandler deploy_contractCompleted;
    
    /// CodeRemarks
    public event available_platformsCompletedEventHandler available_platformsCompleted;
    
    /// CodeRemarks
    public event deploy_contract_callbackCompletedEventHandler deploy_contract_callbackCompleted;
    
    /// CodeRemarks
    public event get_platform_endpointCompletedEventHandler get_platform_endpointCompleted;
    
    /// CodeRemarks
    public event destroyCompletedEventHandler destroyCompleted;
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/platform_deployment_status", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="platform_deployment_status_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string platform_deployment_status([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string platform_id) {
        object[] results = this.Invoke("platform_deployment_status", new object[] {
                    platform_id});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void platform_deployment_statusAsync(string platform_id) {
        this.platform_deployment_statusAsync(platform_id, null);
    }
    
    /// CodeRemarks
    public void platform_deployment_statusAsync(string platform_id, object userState) {
        if ((this.platform_deployment_statusOperationCompleted == null)) {
            this.platform_deployment_statusOperationCompleted = new System.Threading.SendOrPostCallback(this.Onplatform_deployment_statusOperationCompleted);
        }
        this.InvokeAsync("platform_deployment_status", new object[] {
                    platform_id}, this.platform_deployment_statusOperationCompleted, userState);
    }
    
    private void Onplatform_deployment_statusOperationCompleted(object arg) {
        if ((this.platform_deployment_statusCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.platform_deployment_statusCompleted(this, new platform_deployment_statusCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/destroy_platform", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="destroy_platform_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string destroy_platform([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string platform_id) {
        object[] results = this.Invoke("destroy_platform", new object[] {
                    platform_id});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void destroy_platformAsync(string platform_id) {
        this.destroy_platformAsync(platform_id, null);
    }
    
    /// CodeRemarks
    public void destroy_platformAsync(string platform_id, object userState) {
        if ((this.destroy_platformOperationCompleted == null)) {
            this.destroy_platformOperationCompleted = new System.Threading.SendOrPostCallback(this.Ondestroy_platformOperationCompleted);
        }
        this.InvokeAsync("destroy_platform", new object[] {
                    platform_id}, this.destroy_platformOperationCompleted, userState);
    }
    
    private void Ondestroy_platformOperationCompleted(object arg) {
        if ((this.destroy_platformCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.destroy_platformCompleted(this, new destroy_platformCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/deploy", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="deploy_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string deploy([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string profile_id) {
        object[] results = this.Invoke("deploy", new object[] {
                    profile_id});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void deployAsync(string profile_id) {
        this.deployAsync(profile_id, null);
    }
    
    /// CodeRemarks
    public void deployAsync(string profile_id, object userState) {
        if ((this.deployOperationCompleted == null)) {
            this.deployOperationCompleted = new System.Threading.SendOrPostCallback(this.OndeployOperationCompleted);
        }
        this.InvokeAsync("deploy", new object[] {
                    profile_id}, this.deployOperationCompleted, userState);
    }
    
    private void OndeployOperationCompleted(object arg) {
        if ((this.deployCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.deployCompleted(this, new deployCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/available_profiles", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="available_profiles_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlArrayAttribute("result", IsNullable=true)]
    [return: System.Xml.Serialization.XmlArrayItemAttribute("item", IsNullable=false)]
    public profiles_ids[] available_profiles() {
        object[] results = this.Invoke("available_profiles", new object[0]);
        return ((profiles_ids[])(results[0]));
    }
    
    /// CodeRemarks
    public void available_profilesAsync() {
        this.available_profilesAsync(null);
    }
    
    /// CodeRemarks
    public void available_profilesAsync(object userState) {
        if ((this.available_profilesOperationCompleted == null)) {
            this.available_profilesOperationCompleted = new System.Threading.SendOrPostCallback(this.Onavailable_profilesOperationCompleted);
        }
        this.InvokeAsync("available_profiles", new object[0], this.available_profilesOperationCompleted, userState);
    }
    
    private void Onavailable_profilesOperationCompleted(object arg) {
        if ((this.available_profilesCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.available_profilesCompleted(this, new available_profilesCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/deploy_contract", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="deploy_contract_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string deploy_contract([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string contract) {
        object[] results = this.Invoke("deploy_contract", new object[] {
                    contract});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void deploy_contractAsync(string contract) {
        this.deploy_contractAsync(contract, null);
    }
    
    /// CodeRemarks
    public void deploy_contractAsync(string contract, object userState) {
        if ((this.deploy_contractOperationCompleted == null)) {
            this.deploy_contractOperationCompleted = new System.Threading.SendOrPostCallback(this.Ondeploy_contractOperationCompleted);
        }
        this.InvokeAsync("deploy_contract", new object[] {
                    contract}, this.deploy_contractOperationCompleted, userState);
    }
    
    private void Ondeploy_contractOperationCompleted(object arg) {
        if ((this.deploy_contractCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.deploy_contractCompleted(this, new deploy_contractCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/available_platforms", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="available_platforms_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlArrayAttribute("result", IsNullable=true)]
    [return: System.Xml.Serialization.XmlArrayItemAttribute("item", IsNullable=false)]
    public platforms[] available_platforms() {
        object[] results = this.Invoke("available_platforms", new object[0]);
        return ((platforms[])(results[0]));
    }
    
    /// CodeRemarks
    public void available_platformsAsync() {
        this.available_platformsAsync(null);
    }
    
    /// CodeRemarks
    public void available_platformsAsync(object userState) {
        if ((this.available_platformsOperationCompleted == null)) {
            this.available_platformsOperationCompleted = new System.Threading.SendOrPostCallback(this.Onavailable_platformsOperationCompleted);
        }
        this.InvokeAsync("available_platforms", new object[0], this.available_platformsOperationCompleted, userState);
    }
    
    private void Onavailable_platformsOperationCompleted(object arg) {
        if ((this.available_platformsCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.available_platformsCompleted(this, new available_platformsCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/deploy_contract_callback", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="deploy_contract_callback_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string deploy_contract_callback([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string profile_id, [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string core_session_id, [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string remote_ip) {
        object[] results = this.Invoke("deploy_contract_callback", new object[] {
                    profile_id,
                    core_session_id,
                    remote_ip});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void deploy_contract_callbackAsync(string profile_id, string core_session_id, string remote_ip) {
        this.deploy_contract_callbackAsync(profile_id, core_session_id, remote_ip, null);
    }
    
    /// CodeRemarks
    public void deploy_contract_callbackAsync(string profile_id, string core_session_id, string remote_ip, object userState) {
        if ((this.deploy_contract_callbackOperationCompleted == null)) {
            this.deploy_contract_callbackOperationCompleted = new System.Threading.SendOrPostCallback(this.Ondeploy_contract_callbackOperationCompleted);
        }
        this.InvokeAsync("deploy_contract_callback", new object[] {
                    profile_id,
                    core_session_id,
                    remote_ip}, this.deploy_contract_callbackOperationCompleted, userState);
    }
    
    private void Ondeploy_contract_callbackOperationCompleted(object arg) {
        if ((this.deploy_contract_callbackCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.deploy_contract_callbackCompleted(this, new deploy_contract_callbackCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/get_platform_endpoint", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="get_platform_endpoint_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string get_platform_endpoint([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string platform_id) {
        object[] results = this.Invoke("get_platform_endpoint", new object[] {
                    platform_id});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void get_platform_endpointAsync(string platform_id) {
        this.get_platform_endpointAsync(platform_id, null);
    }
    
    /// CodeRemarks
    public void get_platform_endpointAsync(string platform_id, object userState) {
        if ((this.get_platform_endpointOperationCompleted == null)) {
            this.get_platform_endpointOperationCompleted = new System.Threading.SendOrPostCallback(this.Onget_platform_endpointOperationCompleted);
        }
        this.InvokeAsync("get_platform_endpoint", new object[] {
                    platform_id}, this.get_platform_endpointOperationCompleted, userState);
    }
    
    private void Onget_platform_endpointOperationCompleted(object arg) {
        if ((this.get_platform_endpointCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.get_platform_endpointCompleted(this, new get_platform_endpointCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://www.mdcc.ufc.br/hpcshelf/backend/destroy", RequestNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", ResponseElementName="destroy_result", ResponseNamespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
    [return: System.Xml.Serialization.XmlElementAttribute("result", IsNullable=true)]
    public string destroy([System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string endpoint) {
        object[] results = this.Invoke("destroy", new object[] {
                    endpoint});
        return ((string)(results[0]));
    }
    
    /// CodeRemarks
    public void destroyAsync(string endpoint) {
        this.destroyAsync(endpoint, null);
    }
    
    /// CodeRemarks
    public void destroyAsync(string endpoint, object userState) {
        if ((this.destroyOperationCompleted == null)) {
            this.destroyOperationCompleted = new System.Threading.SendOrPostCallback(this.OndestroyOperationCompleted);
        }
        this.InvokeAsync("destroy", new object[] {
                    endpoint}, this.destroyOperationCompleted, userState);
    }
    
    private void OndestroyOperationCompleted(object arg) {
        if ((this.destroyCompleted != null)) {
            System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
            this.destroyCompleted(this, new destroyCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
        }
    }
    
    /// CodeRemarks
    public new void CancelAsync(object userState) {
        base.CancelAsync(userState);
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/")]
public partial class profiles_ids {
    
    private System.Nullable<int> profile_idField;
    
    private string profile_nameField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
    public System.Nullable<int> profile_id {
        get {
            return this.profile_idField;
        }
        set {
            this.profile_idField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
    public string profile_name {
        get {
            return this.profile_nameField;
        }
        set {
            this.profile_nameField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.mdcc.ufc.br/hpcshelf/backend/types/")]
public partial class platforms {
    
    private string platform_idField;
    
    private System.Nullable<int> profile_idField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
    public string platform_id {
        get {
            return this.platform_idField;
        }
        set {
            this.platform_idField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
    public System.Nullable<int> profile_id {
        get {
            return this.profile_idField;
        }
        set {
            this.profile_idField = value;
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void platform_deployment_statusCompletedEventHandler(object sender, platform_deployment_statusCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class platform_deployment_statusCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal platform_deployment_statusCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void destroy_platformCompletedEventHandler(object sender, destroy_platformCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class destroy_platformCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal destroy_platformCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void deployCompletedEventHandler(object sender, deployCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class deployCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal deployCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void available_profilesCompletedEventHandler(object sender, available_profilesCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class available_profilesCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal available_profilesCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public profiles_ids[] Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((profiles_ids[])(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void deploy_contractCompletedEventHandler(object sender, deploy_contractCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class deploy_contractCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal deploy_contractCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void available_platformsCompletedEventHandler(object sender, available_platformsCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class available_platformsCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal available_platformsCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public platforms[] Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((platforms[])(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void deploy_contract_callbackCompletedEventHandler(object sender, deploy_contract_callbackCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class deploy_contract_callbackCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal deploy_contract_callbackCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void get_platform_endpointCompletedEventHandler(object sender, get_platform_endpointCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class get_platform_endpointCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal get_platform_endpointCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
public delegate void destroyCompletedEventHandler(object sender, destroyCompletedEventArgs e);

/// CodeRemarks
[System.CodeDom.Compiler.GeneratedCodeAttribute("wsdl", "0.0.0.0")]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class destroyCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
    
    private object[] results;
    
    internal destroyCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
            base(exception, cancelled, userState) {
        this.results = results;
    }
    
    /// CodeRemarks
    public string Result {
        get {
            this.RaiseExceptionIfNecessary();
            return ((string)(this.results[0]));
        }
    }
}
