class BeamData {
  constructor(L, w1, w2, x) {
    this.L = parseFloat(L);
    this.w1 = parseFloat(w1);
    this.w2 = parseFloat(w2);
    this.x = parseFloat(x);
  }
}

function calculateReactions(beamData, a = 0) {
  const ord1 = (beamData.L - a) / beamData.L;
  const ord2 = (beamData.L - (a + beamData.x)) / beamData.L;
  const RxA = beamData.w1 * ord1 + beamData.w2 * ord2;
  const RxB = beamData.w1 + beamData.w2 - RxA;
  return { RxA, RxB };
}

function findMaxReactions(beamData) {
  let maxRxA = 0.0,
    maxRxB = 0.0,
    posA = 0,
    posB = 0;

  for (let a = 0; a <= beamData.L; a++) {
    const { RxA, RxB } = calculateReactions(beamData, a);
    if (RxA > maxRxA && RxA <= beamData.w1 + beamData.w2) {
      maxRxA = RxA;
      posA = a;
    }
    if (RxB > maxRxB && RxB <= beamData.w1 + beamData.w2) {
      maxRxB = RxB;
      posB = a;
    }
  }

  return {
    maxRxA: maxRxA.toFixed(2),
    posA,
    maxRxB: maxRxB.toFixed(2),
    posB,
  };
}

function calculateBM(beamData, s) {
  let bmOrd2;
  if (s < beamData.x) {
    bmOrd2 =
      ((beamData.L - beamData.x) * (s * (beamData.L - s))) /
      (beamData.L * beamData.L);
  } else {
    bmOrd2 = ((beamData.L - s) * beamData.x) / beamData.L;
  }
  const bm = beamData.w1 * 0 + beamData.w2 * bmOrd2;
  return parseFloat(bm.toFixed(2));
}

function calculateSF(beamData, t) {
  const ord1 = t / beamData.L;
  const ord2 = (t + beamData.x) / beamData.L;

  let Sf;
  if (t < 0.5 * beamData.L) {
    Sf = -(beamData.w1 * ord1 + beamData.w2 * ord2);
  } else if (t > 0.5 * beamData.L && t + beamData.x <= beamData.L) {
    Sf = beamData.w2 * (1 - ord1) + beamData.w1 * (1 - ord2);
  } else {
    Sf = -beamData.w1 * ord2 + beamData.w2 * (1 - ord1);
  }

  return parseFloat(Sf.toFixed(2));
}

function findMaxBM(beamData) {
  let maxVal = 0.0,
    posY = 0;

  for (let y = 0; y <= beamData.L; y++) {
    const ord1 = (y * (beamData.L - y)) / beamData.L;
    const ord2 =
      ((y + beamData.x) * (beamData.L - (y + beamData.x))) / beamData.L;
    const BmY = beamData.w1 * ord1 + beamData.w2 * ord2;

    if (BmY > maxVal) {
      maxVal = parseFloat(BmY.toFixed(2));
      posY = y;
    }
  }

  return { maxBM: maxVal.toFixed(2), posY };
}

function findMaxSF(beamData) {
  let maxVal = 0.0,
    posZ = 0;

  for (let z = 0; z <= beamData.L; z++) {
    const ord1 = z / beamData.L;
    const ord2 = (z + beamData.x) / beamData.L;
    let SfZ;

    if (z > 0.5 * beamData.L) {
      SfZ = beamData.w1 * ord1 + beamData.w2 * ord2;
    } else {
      SfZ = beamData.w2 * ord1 + beamData.w1 * ord2;
    }

    if (SfZ > maxVal) {
      maxVal = SfZ;
      posZ = z;
    }
  }

  return { maxSF: maxVal.toFixed(2), posZ };
}

function analyzeBeam() {
  const L = document.getElementById("length").value;
  const w1 = document.getElementById("w1").value;
  const w2 = document.getElementById("w2").value;
  const x = document.getElementById("distance").value;

  const beamData = new BeamData(L, w1, w2, x);

  const reactions = findMaxReactions(beamData);
  const maxBM = findMaxBM(beamData);
  const maxSF = findMaxSF(beamData);

  const bmList = [];
  for (let s = 0; s <= beamData.L; s++) {
    bmList.push(calculateBM(beamData, s));
  }

  const sfList = [];
  for (let t = 0; t <= beamData.L - beamData.x; t++) {
    sfList.push(calculateSF(beamData, t));
  }

  document.getElementById("reactionResults").innerText = `
        Maximum Rx_A: ${reactions.maxRxA} KN @ w1 at ${reactions.posA} m
        Maximum Rx_B: ${reactions.maxRxB} KN @ w1 at ${reactions.posB} m
    `;

  document.getElementById("sfResults").innerText = `
      
         BM List: ${bmList.join(", ")}
        SF List: ${sfList.join(", ")}
    `;
  document.getElementById("bmResults").innerText = `
    Maximum BM: ${maxBM.maxBM} kN-m @ y = ${maxBM.posY} m
      Maximum SF: ${maxSF.maxSF} kN @ z = ${maxSF.posZ} m
   
`;

  document.getElementById("results").style.display = "block";
}
