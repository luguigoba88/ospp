import {Component, Input, OnInit} from '@angular/core';
import {OsppService} from '../../../ospp.service';

@Component({
  selector: 'app-add-edit-cus',
  templateUrl: './add-edit-cus.component.html',
  styleUrls: ['./add-edit-cus.component.scss']
})
export class AddEditCusComponent implements OnInit {

  constructor(private service: OsppService) { }

  @Input() cus: any;
      CustomerId: string;
      CustomerName: string;
      CustomerName2: string;
      CustomerName3: string;
      Surname: string;
      LastName: string;
      DateOfJoining: string;
      Street: string;
      Number: string;
      Suburb: string;
      ZipCode: string;
      PhotoFileName: string;
      Status: string;
      StatusBC: string;
      StatusWL: string;
      StatusPLD: string;
      PhotoFilePath: string;
      Group: string;

  GroupsList: any = [];

  ngOnInit(): void {
    this.loadGroupList();
  }

  loadGroupList() {
    this.service.getAllGroupNames().subscribe((data: any) => {
      this.GroupsList = data;

      this.CustomerId = this.cus.CustomerId;
      this.CustomerName = this.cus.CustomerName;
      this.CustomerName2 = this.cus.CustomerName2;
      this.CustomerName3 = this.cus.CustomerName3;
      this.Surname = this.cus.Surname;
      this.LastName = this.cus.LastName;
      this.DateOfJoining = this.cus.DateOfJoining;
      this.Street = this.cus.Street;
      this.Number = this.cus.Number;
      this.Suburb = this.cus.Suburb;
      this.ZipCode = this.cus.ZipCode;
      this.PhotoFileName = this.cus.PhotoFileName;
      this.Status = this.cus.Status;
      this.StatusBC = this.cus.StatusBC;
      this.StatusWL = this.cus.StatusWL;
      this.StatusPLD = this.cus.StatusPLD;
      this.PhotoFilePath = this.service.PhotoUrl + this.PhotoFileName;
      this.Group = this.cus.Group;
    });
  }

  addCustomer() {
    var val = {CustomerId: this.CustomerId,
                CustomerName: this.CustomerName,
                CustomerName2: this.CustomerName2,
                CustomerName3: this.CustomerName3,
                Surname: this.Surname,
                LastName: this.LastName,
                DateOfJoining: this.DateOfJoining,
                Street: this.Street,
                Number: this.Number,
                Suburb: this.Suburb,
                ZipCode: this.ZipCode,
                PhotoFileName: this.PhotoFileName,
                Status: this.Status,
                StatusBC: this.StatusBC,
                StatusWL: this.StatusWL,
                StatusPLD: this.StatusPLD,
                Group: this.Group,
    };

    this.service.addCustomer(val).subscribe(res => {
      alert(res.toString());
    });
  }

  updateCustomer() {
    var val = {CustomerId: this.CustomerId,
                CustomerName: this.CustomerName,
                CustomerName2: this.CustomerName2,
                CustomerName3: this.CustomerName3,
                Surname: this.Surname,
                LastName: this.LastName,
                DateOfJoining: this.DateOfJoining,
                Street: this.Street,
                Number: this.Number,
                Suburb: this.Suburb,
                ZipCode: this.ZipCode,
                PhotoFileName: this.PhotoFileName,
                Status: this.Status,
                StatusBC: this.StatusBC,
                StatusWL: this.StatusWL,
                StatusPLD: this.StatusPLD,
                Group: this.Group,
    };

    this.service.updateCustomer(val).subscribe(res => {
      alert(res);
    });
  }


  uploadPhoto(event) {
    var file = event.target.files[0];
    const formData: FormData = new FormData();
    formData.append('uploadedFile', file, file.name);

    this.service.UploadPhoto(formData).subscribe((data: any) => {
      this.PhotoFileName = data.toString();
      this.PhotoFilePath = this.service.PhotoUrl + this.PhotoFileName;
    });
  }

}

