from ecs.entity import Entity
from ecs.time import Time
from ecs.world_clocks import WorldClocks
from core.inventory import Inventory

clocks = WorldClocks(
    Time(minutes=1),
    systems=[

    ]
)

player = Entity(
    Inventory()
)
