#!/usr/bin/env python3
import click
import psutil
import os


@click.group()
def main():
    pass


# Sys status: cpu, mem, hd
@main.command()
def status():
    """ Summary of principal data: cpu, memory and root disk usage. """
    cpu_percent: float = psutil.cpu_percent(interval=0.5)
    mem_info: psutil.svmem = psutil.virtual_memory()
    disk_usage: psutil.sdiskusage = psutil.disk_usage(os.path.sep)

    click.echo(click.style("--- System status ---", fg='cyan', bold=True))
    click.echo(f"CPU utilization: {cpu_percent} %")
    click.echo(f"Total Memory: {mem_info.total / (1024**3):.2f} Go")
    used_memory_gb: float = mem_info.used / (1024**3)
    click.echo(f"Used Memory: {mem_info.percent} % ({used_memory_gb:.2f} Go)")
    click.echo(f"Root Disk Usage: {disk_usage.percent}%")


# Top
@main.command()
@click.option('--sort', '-s',
              default='memory',
              type=click.Choice(['memory', 'cpu']),
              help='Sort by memory or cpu (default is memory)')
@click.option('--limit', '-l',
              default=5,
              type=int,
              help='Number of processes')
def top(sort, limit):
    """ Top command: sort by memory or cpu """

    click.echo(click.style(
        f"--- TOP {limit} processes (sorted by {sort.upper()}) ---",
        fg='magenta',
        bold=True
    ))

    # Get information about processes
    procs: list = []
    for process in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
        try:
            name: str = process.info['name']
            pid: int = process.pid
            cpu_percent: float = process.info['cpu_percent']
            mem: float = process.info['memory_info'].rss / (1024 * 1024)

            procs.append({
                'name': name,
                'pid': pid,
                'cpu_percent': cpu_percent,
                'memory': mem
            })
        except (psutil.NoSuchProcess, AttributeError):
            continue

    # Sort list of processes based on sort option
    key = 'cpu_percent' if sort == 'cpu' else 'memory'
    sorted_procs = sorted(procs, key=lambda x: x[key], reverse=True)

    # Print the list in table and limited by limit option
    click.echo(f"{'PID':<6}{'CPU %':>7}{'MEM (MB)':>10} {'NAME':<30}")
    click.echo("-" * 55)
    for p in sorted_procs[:limit]:
        click.echo(
                f"{p['pid']:<6}{p['cpu_percent']:>7.1f}"
                f"{p['memory']:>10.1f} {p['name']:<30}"
        )


# disks
@main.command()
def disk():
    ''' Information on disk usage '''

    click.echo(click.style(
        "--- Disk Usage ---",
        fg='yellow',
        bold=True
    ))

    click.echo(
            f"{'Device':<25}{'Mountpoint':<20}"
            f"{'Disk Usage %':>15} {'FS type':>10}"
    )
    click.echo("-" * 70)

    # Get partition information
    for partition in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            click.echo(
                    f"{partition.device:<25}{partition.mountpoint:<20}"
                    f"{usage.percent:>15}{partition.fstype:>10}"
            )
        except (PermissionError):
            continue


# Entry of the command
if __name__ == "__main__":
    main()
