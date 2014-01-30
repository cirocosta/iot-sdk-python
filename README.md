Concurso IoT Telefonica
===

iot-telefonica-cpbr7
Tema sorteado: **emprego**, **enchentes**.
token: @secrets



Estrutura
===
Todo o código sera processado e armazenado no GAE, que por CRON irá dar um fetch em toda informação enviada pelo mesmo para o cloud.


DCA
===
> Plataforma cloud da Telefonica.

Para o concurso há basicamente apenas uma entrada, a referente a seu serviço, sendo então ramificada para informações do(s) aparelho(s).

base path: `http://dca.telefonicabeta.com/m2m/v2/`


Detalhes to serviço
---
**GET**
```
services/{token}
```

**Response**:
```
data
    GENERATED_UNIQUE_IDENTIFIER
    acl
        user
        description
        export
        subscription
        command
        query
        whiteList
        blackList
        waitingList
        creationTime
        actions
        config
            defaultStats
            normalizedParams
            notification
            qualityOfService
            ruleEngine
            storage
            status
            activate
            rushIntervals
            accumulateBy
        creationTime
        description
        legact
        name
        organizationId
        updateTime
        stats
            devicesRegistred
            trafficMessages
            storageSpaceMB
        appId
``` 

Aparelhos Conectados
---
**GET**
```
services/{token}/assets
```

**Parameters for the request**

-   limit


**RESPONSE**
count
data
    asset
    name


Dados vindos do aparelho
---
**GET**
```
services/{token}/assets/{token}
```

**RESPONSE**
```
data
    DeviceProps
        commandURL
        manufacturer
        model
        serialNumber
        version
        lastIP
        commands
    asset
        ...
    creationTime
    isConcentrator
    model
    name
    registrationTime
    status
    sensorData
        st
        ms
            v
            p
            u    

```

Medidas do aparelho
---
**GET**
```
/services/{token}/assets/{token}/data
```

**Params**

-   limit
-   offset
-   sortBy
    --  samplingTime

**RESPONSE**
```
das
```

