<%@ WebService Language="C#" Class="AddSimpleWebService.AddSimple" %>
using System;
using System.Web;
using System.Web.Services;

namespace AddSimpleWebService
{
	[WebService]
	public class AddSimple : System.Web.Services.WebService
	{
	    [WebMethod]
		public String add_simple(String a, String b)
		{
		 	return a + b;
		}
	}
}

