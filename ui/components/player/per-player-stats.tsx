import * as React from 'react';
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';
import { PerPlayerStat } from 'tntfl-api';

import GamesChart from '../games-chart';
import PlayerName from '../player-name';

interface HeadToHeadLinkProps {
  base: string;
  player1: string;
  player2: string;
}
function HeadToHeadLink(props: HeadToHeadLinkProps): JSX.Element {
  const { base, player1, player2 } = props;
  return (
    <a href={`${base}headtohead/${player1}/${player2}/`}>
      ⇋
    </a>
  );
}

function toTableData(stats: PerPlayerStat[]) {
  return stats && stats.sort((a: PerPlayerStat, b: PerPlayerStat) => b.skillChange - a.skillChange).map((s) => {
    return {
      opponent: s.opponent,
      for: s.for,
      against: s.against,
      games: s.games,
      wins: s.wins,
      draws: s.games - s.wins - s.losses,
      losses: s.losses,
      totals: {
        for: s.for,
        against: s.against,
        games: s.games,
        wins: s.wins,
        losses: s.losses,
      },
      skillChange: s.skillChange.toFixed(3),
    };
  });
}

interface PerPlayerStatsProps {
  playerName: string;
  base: string;
  stats: PerPlayerStat[];
}
export default function PerPlayerStats(props: PerPlayerStatsProps): JSX.Element {
  const { playerName, base, stats } = props;
  return (
    <BootstrapTable
      data={toTableData(stats)}
      hover={true}
      condensed={true}
      bodyStyle={{fontSize: 20}}
    >
      <TableHeaderColumn dataField={'opponent'} dataSort={true} isKey={true} dataFormat={(n) => <PlayerName base={base} name={n}/>}>Opponent</TableHeaderColumn>
      <TableHeaderColumn dataField={'opponent'} dataFormat={(n) => <HeadToHeadLink player1={playerName} player2={n} base={base}/>} dataAlign={'center'} width={'30'}></TableHeaderColumn>
      <TableHeaderColumn dataField={'totals'} dataFormat={(p) => GamesChart(p)}>Games</TableHeaderColumn>
      <TableHeaderColumn dataField={'games'} dataSort={true} dataAlign={'center'}>Games</TableHeaderColumn>
      <TableHeaderColumn dataField={'wins'} dataSort={true} dataAlign={'center'}>Wins</TableHeaderColumn>
      <TableHeaderColumn dataField={'draws'} dataSort={true} dataAlign={'center'}>Draws</TableHeaderColumn>
      <TableHeaderColumn dataField={'losses'} dataSort={true} dataAlign={'center'}>Losses</TableHeaderColumn>
      <TableHeaderColumn dataField={'for'} dataSort={true} dataAlign={'center'}>For</TableHeaderColumn>
      <TableHeaderColumn dataField={'against'} dataSort={true} dataAlign={'center'}>Against</TableHeaderColumn>
      <TableHeaderColumn dataField={'skillChange'} dataSort={true} dataAlign={'center'}>Skill Change</TableHeaderColumn>
    </BootstrapTable>
  );
}
