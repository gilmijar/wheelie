from tomllib import load as toml_load

conf = toml_load(open("config.toml", "rb"))
print(conf)
