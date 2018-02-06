from fractions import gcd


def check_corners(dimensions, captain_position, d):
    corners = {1: [0, 0],
               2: [0, dimensions[1]],
               3: [dimensions[0], dimensions[1]],
               4: [dimensions[0], 0]}
    for corner in corners.values():
        if (corner[1]-captain_position[1])*d[0] == (corner[0] -
                                                    captain_position[0])*d[1]:
            return False
    return True


def answer(dimensions, captain_position, badguy_position, distance):
    # your code here
    maxreflectx = distance / dimensions[0] + 2
    maxreflecty = distance / dimensions[1] + 2
    virtual_captain = [captain_position[0], captain_position[1]]
    virtual_badguy = [badguy_position[0], badguy_position[1]]

    badguy_shots = {}
    self_shots = {}
    for xref in xrange(-maxreflectx, maxreflectx):
        for yref in xrange(-maxreflecty, maxreflecty):
            if (xref > 0 and xref % 2 != 0) or (xref < 0 and xref % 2 == 0):
                virtual_captain[0] = (dimensions[0] - captain_position[0] +
                                      (abs(xref) - (1 if xref < 0 else 0)) *
                                      dimensions[0]) * (1 if xref >= 0 else -1)
                virtual_badguy[0] = (dimensions[0] - badguy_position[0] +
                                     (abs(xref) - (1 if xref < 0 else 0)) *
                                     dimensions[0]) * (1 if xref >= 0 else -1)
            else:
                virtual_captain[0] = (captain_position[0] + (abs(xref) -
                                      (1 if xref < 0 else 0.0)) *
                                      dimensions[0]) * (1 if xref >= 0 else -1)
                virtual_badguy[0] = (badguy_position[0] + (abs(xref) -
                                     (1 if xref < 0 else 0.0)) *
                                     dimensions[0]) * (1 if xref >= 0 else -1)

            if (yref > 0 and yref % 2 != 0) or (yref < 0 and yref % 2 == 0):
                virtual_captain[1] = (dimensions[1] - captain_position[1] +
                                      (abs(yref) - (1 if yref < 0 else 0)) *
                                      dimensions[1]) * (1 if yref >= 0 else -1)
                virtual_badguy[1] = (dimensions[1] - badguy_position[1] +
                                     (abs(yref) - (1 if yref < 0 else 0)) *
                                     dimensions[1]) * (1 if yref >= 0 else -1)
            else:
                virtual_captain[1] = (captain_position[1] +
                                      (abs(yref) - (1 if yref < 0 else 0)) *
                                      dimensions[1]) * (1 if yref >= 0 else -1)
                virtual_badguy[1] = (badguy_position[1] +
                                     (abs(yref) - (1 if yref < 0 else 0)) *
                                     dimensions[1]) * (1 if yref >= 0 else -1)

            self_shot = [virtual_captain[0] - captain_position[0],
                         virtual_captain[1] - captain_position[1]]
            badguy_shot = [virtual_badguy[0] - captain_position[0],
                           virtual_badguy[1] - captain_position[1]]

            f1 = abs(gcd(self_shot[0], self_shot[1]))
            f2 = abs(gcd(badguy_shot[0], badguy_shot[1]))

            l1 = (self_shot[0]**2 + self_shot[1]**2)**(0.5)
            l2 = (badguy_shot[0]**2 + badguy_shot[1]**2)**(0.5)

            if l1 <= distance and f1 > 0:
                self_shots[(self_shot[0]//f1, self_shot[1]//f1)] = \
                 min(l1, self_shots.get((self_shot[0]//f1, self_shot[1]//f1),
                     l1))
                if (self_shots[(self_shot[0]//f1, self_shot[1]//f1)] <
                   (0 if f1 == 0 else badguy_shots.get((self_shot[0]//f1,
                                                        self_shot[1]//f1),
                                                       distance))):
                    badguy_shots.pop((self_shot[0]//f1, self_shot[1]//f1),
                                     None)

            if (l2 <= distance):
                badguy_shots[(badguy_shot[0]//f2, badguy_shot[1]//f2)] = \
                 min(l2, badguy_shots.get((badguy_shot[0]//f2,
                                           badguy_shot[1]//f2), l2))
                if (badguy_shots[(badguy_shot[0]//f2, badguy_shot[1]//f2)] >
                   (0 if f2 == 0 else self_shots.get((badguy_shot[0]//f2,
                                                      badguy_shot[1]//f2),
                                                     distance))):
                    badguy_shots.pop((badguy_shot[0]//f2, badguy_shot[1]//f2),
                                     None)

    return len(badguy_shots)
