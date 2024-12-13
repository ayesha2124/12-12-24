project = float(input("Enter project score: "))
internal = float(input("Enter internal score: "))
external = float(input("Enter external score: "))
if project < 50 and internal < 50 and external < 50:
    print(f"Failed in project: {project}, internal: {internal}, and external: {external}")
elif project < 50 and internal < 50:
    print(f"Failed in project: {project} and internal: {internal}")
elif project < 50 and external < 50:
    print(f"Failed in project: {project} and external: {external}")
elif internal < 50 and external < 50:
    print(f"Failed in internal: {internal} and external: {external}")
elif project < 50:
    print(f"Failed in project: {project}")
elif internal < 50:
    print(f"Failed in internal: {internal}")
elif external < 50:
    print(f"Failed in external: {external}")
else:
    total = (project * 0.70) + (internal * 0.10) + (external * 0.20)
    if total > 90:
        print(f"Passed with grade A (Total: {total})")
    elif total >= 80:
        print(f"Passed with grade B (Total: {total})")
    elif total >= 70:
        print(f"Passed with grade C (Total: {total})")
    else:
        print(f"Failed due to total score being below 70 (Total: {total})")
