import { Component } from '@angular/core';

@Component({
  templateUrl: 'leads.component.html'
})
export class LeadsComponent {

  constructor() { }

  isCollapsed: boolean = false;

  collapsed(event: any): void {
    // console.log(event);
  }

  expanded(event: any): void {
    // console.log(event);
  }

}
