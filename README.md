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
- name: Demo rules with websocket as source
  hosts: all

  sources:
    - name: websocket
      smartgic.eda.websocket:
        host: "{{ websocket_host | default('127.0.0.1') }}"
        port: "{{ websocket_port | default(8181) }}"
        path: "{{ websocket_path | default('/core') }}"

  rules:
    - name: Run job template
      condition: event.type == "ovos-skill-personal.OpenVoiceOS:WhoMadeYou.intent"
      action:
        run_job_template:
          name: OVOS History
          organization: Default
          job_args:
            extra_vars:
              which_user: Gaetan
          retries: 2
          delay: 10
```

In order to pass the `extra_vars` make sure to check "Prompt on Launch" within the job template, *cf:* https://github.com/ansible/ansible-rulebook/issues/622

## Build DE (Decision Envionrment)

```shell
git clone https://github.com/smartgic/eda.git
cd eda
pip install ansible-builder
ansible-builder build -f decision-environment.yml -t smartgic/de-custom:latest -t smartgic/de-custom:1.0.2
podman push smartgic/de-custom:latest
```
