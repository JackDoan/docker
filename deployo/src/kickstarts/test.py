from deployo.src.kickstarts.kickstart_generator import KickstartGenerator

kg = KickstartGenerator()
print("Kickstart File:\n")
print(kg.get("swarm-node"))
print("\n\n#############################\n\nFirstboot Script:\n")
print(kg.get_firstboot("swarm-node"))
print("#############################\n")
