# Event Driven Automation Collection

This collection was born with the idea to group some plugins and resources that can be helpful in extending the Event Driven Automation collection.

## Plugins

The following plugins are included in this collection:

| Name                   | Description                      |
| ---------------------- | -------------------------------- |
| smartgic.eda.websocket | Listen to a websocket for events |

### Usage

A sample rulebook using `smartgic.eda.websocket` source plugin is shown below:

```yaml
---
- name: Websocket as source plugin
  hosts: all

  sources:
    - name: websocket
      smartgic.eda.websocket:
        host: localhost
        port: 8181
        path: /core

  rules:
    - name: Check for message type
      condition: event.type == "ovos-skill-personal.OpenVoiceOS.activate"
      action:
        debug:
```