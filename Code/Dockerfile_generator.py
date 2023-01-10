def dockerfileGenerator(from_image, copy_files, add_files, env_vars, run_commands, volume_mounts, user, workdir,
                        expose_ports):
    dockerfile = f"FROM {from_image}\n"

    # Add COPY instructions
    for src_file in copy_files:
        dockerfile += f"COPY {src_file} {src_file}\n"

    # Add ADD instructions
    for src_file in add_files:
        dockerfile += f"ADD {src_file} {src_file}\n"

    # Add ENV instructions
    for key, value in env_vars.items():
        dockerfile += f"ENV {key} {value}\n"

    # Add RUN instructions
    for command in run_commands:
        dockerfile += f"RUN {command}\n"

    # Add VOLUME instructions
    for mount in volume_mounts:
        dockerfile += f"VOLUME {mount}\n"

    # Set USER
    dockerfile += f"USER {user}\n"

    # Set WORKDIR
    dockerfile += f"WORKDIR {workdir}\n"

    # Add EXPOSE instructions
    for port in expose_ports:
        dockerfile += f"EXPOSE {port}\n"

    # Open file in write mode
    with open("Dockerfile", "w") as f:
        # Write Dockerfile to file
        f.write(dockerfile)