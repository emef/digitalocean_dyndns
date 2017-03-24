# digitalocean_dyndns
quick script to use digitalocean as a dynamic dns

Updates a specfied dns record managed by digitalocean to point to the
machine's current IP address. This emulates basic functionality of
dynamic dns without the cost.

-----

## Config

Configuration is done via environment variables, the following MUST be set.

`DIGITALOCEAN_API_KEY` - digitalocean API token
`DIGITALOCEAN_DOMAIN` - domain being managed by digitalocean
`DIGITALOCEAN_DNS_NAME` - name of the dns record (created in the ui) to update

-----

## Usage

Set up your environment variables and run dyndns.py, I set it up as a
cron on my home machine to use it keep it in sync.