# Azure SAML Proxy

**NOT FOR PRODUCTION**

An example of SATOSA as a proxy between Azure and Skolfederation Trial.
SATOSA and pyFF are built from source code, but it should be easy to modify
 so that eg PyPi is used.


## Prerequisites

### Build Images

Build the base image and the image used to build the wheels.


```
docker-compose -f docker-compose-build.yaml build
```

Build wheels.

```
docker-compose -f docker-compose-build.yaml run --rm py-builder
```

### Configuration
Change the configuration for the SATOSA backend found in
```
./satosa/opt/satosa/plugins/backends/
```

## Start the application.

Containers:  

- **proxy-idp-nginx:** Revproxy  
- **proxy-idp-pyff:** mdq server  
- **proxy-idp-satosa:** SATOSA proxy

Create and start containers.
```
docker-compose up
```


## Test

The proxy is registerd in Skolfederation Trial

**entityID:** https://proxy-idp.labb.swefed.se/Saml2IDP/proxy.xml  
**Display Name:** Skolfederation Proxy

The hostname for the revproxy is registerd in public DNS.

**Hostname:** proxy-idp.labb.swefed.se  
**IP:** 127.0.0.1

If the application runs on localhost and also the browser everything should work.


Open URL in a browser.

https://sp.trial.skolfederation.swefed.se/

From the drop-down list select "Skolfederation Proxy" and accept the self signed certificate.
