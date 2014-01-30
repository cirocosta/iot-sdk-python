IoT-sdk for Python
===

Estrutura
---
```
.env/                   -- environmental path do virtualenv
src/                    -- código
    iotsdk.py           -- bibliteca
    secrets.py          -- contém o token
    tests.py            -- testes (sem divisão por tipo)
requirements.txt        -- dev dependencies
```

Install
---

Instale o virtualenv

```bash
$ pip install virtualenv
```

Crie o ambiente
```bash
$ virtualenv .env
```

Ative o ambiente
```bash
$ source .env/bin/activate
```

Rode os testes
```bash
$ cd src/
$ nosetests --verbose
```

Se tudo estiver ok, basta utilizar como indicado na próxima sessão

Utilizando
---

```python
from iotsdk import Iot
import secrets

iot = Iot(secrets.MY_TOKEN)

iot.get_services_details()
iot.get_connected_devices()
iot.get_device_data()
iot.get_device_data(limit=10)
iot.get_device_full_data()
```

DCA
---
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

**RESPONSE**
```
count
data
    asset
    name
```

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
asset
count
data
```

Contributing
===
see `CONTRIBUTING.md` file.
