const pptxgen = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/pptxgenjs');
const fs = require('fs');
const path = require('path');

const IMGDIR = '/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/pptimg';
const OUT = '/home/user/edgevision-pro/deck/EdgeVision-Fabric-Lens.pptx';

const pres = new pptxgen();
// Exact PowerPoint 16:9 widescreen deck size
pres.defineLayout({ name: 'PPT16x9', width: 13.333, height: 7.5 });
pres.layout = 'PPT16x9';
pres.author = 'Pattern AI Labs';
pres.company = 'Pattern AI Labs';
pres.subject = 'EdgeVision Fabric Lens';
pres.title = 'EdgeVision Fabric Lens';

const files = fs.readdirSync(IMGDIR).filter(f => /^slide-\d+\.png$/.test(f)).sort();

// Speaker-note context per slide (matches the running header context)
const ctx = [
  'Cover — EdgeVision Fabric Lens · Pattern AI Labs',
  'Positioning — one edge platform, one QSR vision lens',
  'Problem — the visibility gap',
  'Problem — the compounding cost',
  'Solution — a vision system that intervenes',
  'Solution — the intervention loop',
  'Tech — five techniques, one vision system',
  'Tech — object detection & classification',
  'Tech — action recognition & tracking/re-ID',
  'Tech — signal fusion (the moat)',
  'Tech — custom-model lifecycle',
  'Value — six P&L-tied measurement categories',
  'Value — the fusion-only KPIs (the moat)',
  'Use cases — QSR: speed, accuracy, safety',
  'Use cases — drive-thru & every service window',
  'Use cases — retail store floor (two lenses)',
  'Platform — product architecture (three zones)',
  'Platform — Intel hardware & privacy by design',
  'Why — the paradigm shift',
  'Proof — production lineage',
  'Engagement — pilot to production to chain rollout',
  'Closing — see every station, catch every drift, intervene',
];

files.forEach((f, i) => {
  const slide = pres.addSlide();
  slide.background = { color: '000000' };
  slide.addImage({
    path: path.join(IMGDIR, f),
    x: 0, y: 0, w: 13.333, h: 7.5,
    sizing: { type: 'cover', w: 13.333, h: 7.5 },
  });
  if (ctx[i]) slide.addNotes(ctx[i]);
});

pres.writeFile({ fileName: OUT }).then(() => {
  console.log('WROTE', OUT, 'with', files.length, 'slides');
}).catch(e => { console.error(e); process.exit(1); });
