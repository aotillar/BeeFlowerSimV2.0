from BFS.simulation import entity, mediator


def main_loop():
    mdr = mediator.Mediator()
    c1 = entity.WorldEntity(mdr, 'c1')
    c2 = entity.WorldEntity(mdr, 'c2')
    c3 = entity.WorldEntity(mdr, 'c3')

    mdr.add(c1)
    mdr.add(c2)
    mdr.add(c3)

    x = 0
    while x == 0:
        c1.update()
        c2.update()
        c3.update()


if __name__ == '__main__':
    main_loop()