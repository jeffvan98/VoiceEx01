# WebHook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | **str** | The location of this entity. | [optional] 
**display_name** | **str** | The display name of the object. | 
**description** | **str** | The description of the object. | [optional] 
**custom_properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
**properties** | [**WebHookProperties**](WebHookProperties.md) |  | [optional] 
**web_url** | **str** | The registered URL that will be used to send the POST requests for the registered events to. | 
**events** | [**WebHookEvents**](WebHookEvents.md) |  | 
**created_date_time** | **datetime** | The time-stamp when the object was created. The time stamp is encoded as ISO 8601 date and time format (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered. The time stamp is encoded as ISO 8601 date and time format (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**links** | [**WebHookLinks**](WebHookLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


